"""Synthetic ZIP/IMG audit tests, no real OEM content."""
import hashlib
import importlib.util
from pathlib import Path
import struct
import sys
import tempfile
import unittest
import warnings
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("backup_audit", ROOT / "tools/audit_backup_archives.py")
MOD = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MOD
SPEC.loader.exec_module(MOD)


def sidecar(data, name="test.img"):
    return ("{}  {}\n".format(hashlib.sha256(data).hexdigest(), name)).encode("ascii")


class ArchiveTests(unittest.TestCase):
    def test_zip_valid(self):
        with tempfile.TemporaryDirectory() as d:
            data = b"synthetic firmware substitute" * 300
            with ZipFile(Path(d) / "test.zip", "w", ZIP_DEFLATED) as z:
                z.writestr("backup/test.img", data)
                z.writestr("backup/test.img.sha256", sidecar(data))
                z.writestr("notes.txt", b"ordinary text")
            r = MOD.audit_folder(Path(d))
            self.assertEqual((r.archives, r.crc_pass, r.images, r.match, r.exit_code()), (1, 1, 1, 1, 0))

    def test_local_img_valid(self):
        with tempfile.TemporaryDirectory() as d:
            data = b"fake data"
            (Path(d) / "test.img").write_bytes(data)
            (Path(d) / "test.img.sha256").write_bytes(sidecar(data))
            r = MOD.audit_folder(Path(d))
            self.assertEqual((r.match, r.exit_code()), (1, 0))

    def test_zip_without_sidecar_is_review(self):
        with tempfile.TemporaryDirectory() as d:
            with ZipFile(Path(d) / "test.zip", "w") as z:
                z.writestr("test.img", b"test")
            r = MOD.audit_folder(Path(d))
            self.assertEqual((r.review, r.match, r.exit_code()), (1, 0, 1))

    def test_hash_mismatch_is_error_status(self):
        with tempfile.TemporaryDirectory() as d:
            with ZipFile(Path(d) / "test.zip", "w") as z:
                z.writestr("test.img", b"different")
                z.writestr("test.img.sha256", sidecar(b"original"))
            r = MOD.audit_folder(Path(d))
            self.assertEqual((r.mismatch, r.exit_code()), (1, 2))

    def test_wrong_sidecar_filename(self):
        with tempfile.TemporaryDirectory() as d:
            with ZipFile(Path(d) / "test.zip", "w") as z:
                z.writestr("test.img", b"data")
                z.writestr("test.img.sha256", sidecar(b"data", "../test.img"))
            r = MOD.audit_folder(Path(d))
            self.assertGreater(r.error, 0)

    def test_zip_path_traversal_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            with ZipFile(Path(d) / "test.zip", "w") as z:
                z.writestr("../test.img", b"bad path")
            r = MOD.audit_folder(Path(d))
            self.assertEqual(r.exit_code(), 2)

    def test_duplicate_member_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                with ZipFile(Path(d) / "test.zip", "w") as z:
                    z.writestr("test.img", b"a")
                    z.writestr("test.img", b"b")
            r = MOD.audit_folder(Path(d))
            self.assertGreater(r.error, 0)

    def test_crc_failure(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "test.zip"
            data = b"crc test"
            with ZipFile(path, "w", ZIP_DEFLATED) as z:
                z.writestr("test.img", data)
                z.writestr("test.img.sha256", sidecar(data))
            raw = bytearray(path.read_bytes())
            offset = raw.index(b"PK\x01\x02") + 16
            struct.pack_into("<I", raw, offset, 0x12345678)
            path.write_bytes(raw)
            r = MOD.audit_folder(Path(d))
            self.assertEqual(r.crc_pass, 0)
            self.assertEqual(r.exit_code(), 2)

    def test_zip_without_img_not_pass(self):
        with tempfile.TemporaryDirectory() as d:
            with ZipFile(Path(d) / "test.zip", "w") as z:
                z.writestr("notes.txt", b"text")
            self.assertEqual(MOD.audit_folder(Path(d)).exit_code(), 2)

    def test_standalone_without_sidecar_is_review(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / "test.img").write_bytes(b"data")
            self.assertEqual(MOD.audit_folder(Path(d)).exit_code(), 1)

    def test_symlink_to_img_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / "base.img").write_bytes(b"data")
            try:
                (root / "alias.img").symlink_to("base.img")
            except (OSError, NotImplementedError):
                self.skipTest("No symlinks available")
            r = MOD.audit_folder(root)
            self.assertGreater(r.error, 0)

    def test_archive_limit(self):
        with tempfile.TemporaryDirectory() as d:
            with ZipFile(Path(d) / "test.zip", "w") as z:
                z.writestr("test.img", b"data")
            old = MOD.MAX_MEMBERS
            MOD.MAX_MEMBERS = 0
            try:
                r = MOD.audit_folder(Path(d))
            finally:
                MOD.MAX_MEMBERS = old
            self.assertGreater(r.error, 0)


if __name__ == "__main__":
    unittest.main()
