"""Synthetic-only safety tests for the source-only H01 unlock/root helpers.

No phone, EDL programmer, OEM boot image or network access required.
"""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]


def import_file(name, path):
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


unlock = import_file("h01_unlock_offline", ROOT / "tools/h01_unlock/offline_devinfo.py")
root = import_file("h01_root_host", ROOT / "tools/h01_root/root_tool.py")


class DevinfoTests(unittest.TestCase):
    def setUp(self):
        self.original = (unlock.OLD_MAGIC + b"\0" * 3 +
                         b"\0" * (unlock.SIZE - 16))

    def test_valid_candidate_changes_only_12_magic_bytes(self):
        candidate = unlock.prepare_candidate(self.original)
        report = unlock.inspect(self.original, candidate)
        self.assertEqual(report["changed_byte_count"], 12)
        self.assertTrue(report["offline_verified"])
        self.assertFalse(report["device_unlocked"])
        self.assertEqual(candidate[13:], self.original[13:])

    def test_tampered_candidate_rejected(self):
        candidate = bytearray(unlock.prepare_candidate(self.original))
        candidate[0x100] = 1
        with self.assertRaises(ValueError):
            unlock.inspect(self.original, bytes(candidate))

    def test_unexpected_magic_rejected(self):
        with self.assertRaises(ValueError):
            unlock.prepare_candidate(b"X" + self.original[1:])

    def test_already_unlocked_record_rejected(self):
        data = bytearray(self.original)
        data[0x10] = 1
        with self.assertRaises(ValueError):
            unlock.prepare_candidate(bytes(data))

    def test_create_needs_explicit_confirmation_and_does_not_overwrite(self):
        with tempfile.TemporaryDirectory() as td:
            d = Path(td)
            original = d / "orig.img"
            aboot = d / "aboot.img"
            output = d / "candidate.img"
            original.write_bytes(self.original)
            aboot.write_bytes(b"\x7fELF" + b"\0" * (unlock.SIZE - 4))
            argv = ["prepare", "--devinfo", str(original),
                    "--expected-devinfo", unlock.sha256(self.original),
                    "--aboot", str(aboot),
                    "--expected-aboot", unlock.sha256(aboot.read_bytes()),
                    "--candidate", str(output)]
            with self.assertRaises(ValueError):
                unlock.main(argv)
            self.assertFalse(output.exists())
            self.assertEqual(unlock.main(argv + ["--confirm", "PREPARE-MY-OWN-H01"]), 0)
            self.assertTrue(output.exists())
            with self.assertRaises(ValueError):
                unlock.main(argv + ["--confirm", "PREPARE-MY-OWN-H01"])


class RootTests(unittest.TestCase):
    def test_sha_validation(self):
        self.assertEqual(root.checked_digest("A" * 64), "a" * 64)
        with self.assertRaises(ValueError):
            root.checked_digest("PLACEHOLDER")

    def test_private_config_requires_serial(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "config.local.json"
            p.write_text(json.dumps({
                "serial": "serial with spaces",
                "stock_image": "a.img",
                "patched_image": "b.img",
                "stock_sha256": "a" * 64,
                "patched_sha256": "b" * 64
            }))
            with self.assertRaises(ValueError):
                root.load_config(str(p))

    def test_flash_actions_stop_without_confirmation(self):
        sample = {"serial": "testserial", "stock_sha256": "a" * 64,
                  "patched_sha256": "b" * 64}
        with mock.patch.object(root, "load_config", return_value=sample), \
             mock.patch.object(root, "verify_images", return_value=True), \
             mock.patch.object(root, "root_check") as check:
            with self.assertRaises(ValueError):
                root.main(["flash-root", "--config", "not-used.json"])
            with self.assertRaises(ValueError):
                root.main(["restore-stock", "--config", "not-used.json"])
            check.assert_not_called()

    def test_root_script_never_bundles_device_hashes(self):
        src = (ROOT / "tools/h01_root/root_tool.py").read_text()
        self.assertNotIn("dcaf9613", src)
        self.assertNotIn("c099f23b", src)
        self.assertNotIn("a52afc74197f9e5", src)


if __name__ == "__main__":
    unittest.main()
