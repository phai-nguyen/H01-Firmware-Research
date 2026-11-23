"""Checks for sanitized GPT CSV and offline SHA-256 verification."""
import csv
import hashlib
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("verify_sha256", ROOT / "tools/verify_sha256.py")
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class PartitionMapTests(unittest.TestCase):
    def test_gpt_snapshot_is_sanitized_and_consistent(self):
        path = ROOT / "docs/firmware/partition-layout-sanitized.csv"
        with path.open(encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            self.assertEqual(reader.fieldnames, ["index", "name", "start_lba", "end_lba", "sectors", "size_bytes"])
            rows = list(reader)
        self.assertEqual(len(rows), 42)
        previous = 0
        for i, row in enumerate(rows, 1):
            self.assertEqual(int(row["index"]), i)
            start, end = int(row["start_lba"]), int(row["end_lba"])
            sectors = int(row["sectors"])
            self.assertGreater(start, previous)
            self.assertGreaterEqual(end, start)
            self.assertEqual(end - start + 1, sectors)
            self.assertEqual(sectors * 512, int(row["size_bytes"]))
            previous = end
        self.assertEqual(rows[10]["name"], "boot")
        self.assertEqual(rows[41]["name"], "userdata")
        self.assertEqual(int(rows[41]["end_lba"]), 15269854)


class BackupChecksumTests(unittest.TestCase):
    def test_valid_sha256sum_sidecar(self):
        with tempfile.TemporaryDirectory() as d:
            folder = Path(d)
            data = b"synthetic example - not firmware"
            (folder / "example.img").write_bytes(data)
            digest = hashlib.sha256(data).hexdigest()
            sidecar = folder / "example.img.sha256"
            sidecar.write_text("{}  example.img\n".format(digest), encoding="ascii")
            ok, message = MOD.verify(sidecar)
            self.assertTrue(ok)
            self.assertTrue(message.startswith("PASS:"))

    def test_mismatched_hash(self):
        with tempfile.TemporaryDirectory() as d:
            folder = Path(d)
            (folder / "example.img").write_bytes(b"different")
            sidecar = folder / "example.img.sha256"
            sidecar.write_text("{}  example.img\n".format("a" * 64), encoding="ascii")
            ok, message = MOD.verify(sidecar)
            self.assertFalse(ok)
            self.assertIn("MISMATCH", message)

    def test_traversal_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            sidecar = Path(d) / "escape.sha256"
            sidecar.write_text("{}  ../userdata.img\n".format("0" * 64), encoding="ascii")
            ok, message = MOD.verify(sidecar)
            self.assertFalse(ok)
            self.assertIn("unsafe", message)

    def test_missing_target_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            sidecar = Path(d) / "missing.sha256"
            sidecar.write_text("{}  missing.img\n".format("0" * 64), encoding="ascii")
            ok, message = MOD.verify(sidecar)
            self.assertFalse(ok)
            self.assertIn("missing", message)


if __name__ == "__main__":
    unittest.main()
