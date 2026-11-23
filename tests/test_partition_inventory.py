"""Synthetic inventory tests. No H01 OEM backup files."""
import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("partition_inventory", ROOT / "tools/audit_partition_inventory.py")
MOD = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MOD
SPEC.loader.exec_module(MOD)


def csv_source(folder):
    p = folder / "gpt.csv"
    p.write_text(
        "index,name,start_lba,end_lba,sectors,size_bytes\n"
        "1,boot,100,101,2,1024\n"
        "2,modem,102,104,3,1536\n", encoding="utf-8")
    return p


class InventoryTests(unittest.TestCase):
    def test_full_candidate_coverage_local_and_zip(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d)
            gpt = MOD.load_gpt(csv_source(f))
            (f / "H01-boot-20261111.img").write_bytes(b"a" * 1024)
            with ZipFile(f / "backup.zip", "w") as z:
                z.writestr("H01-modem-20261111.img", b"b" * 1536)
            r = MOD.audit(f, gpt)
            self.assertEqual((len(r.found), len(r.missing), r.exit_code()), (2, 0, 0))

    def test_missing_partition_is_not_full_coverage(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d)
            gpt = MOD.load_gpt(csv_source(f))
            (f / "H01-boot-20261111.img").write_bytes(b"a" * 1024)
            r = MOD.audit(f, gpt)
            self.assertEqual(r.missing, {"modem"})
            self.assertEqual(r.exit_code(), 1)

    def test_wrong_size_fails_coverage(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d)
            gpt = MOD.load_gpt(csv_source(f))
            (f / "H01-boot-20261111.img").write_bytes(b"a")
            r = MOD.audit(f, gpt)
            self.assertIn("boot", r.size_disagreement)
            self.assertIn("boot", r.missing)

    def test_exclude_modified_boot_marker(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d)
            gpt = MOD.load_gpt(csv_source(f))
            (f / "H01-boot-RAM-MARKER-20261111.img").write_bytes(b"a" * 1024)
            r = MOD.audit(f, gpt)
            self.assertEqual(len(r.found), 0)
            self.assertEqual(r.ignored, 1)

    def test_duplicate_versions_still_one_partition(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d)
            gpt = MOD.load_gpt(csv_source(f))
            (f / "H01-boot-20261110.img").write_bytes(b"a" * 1024)
            (f / "H01-boot-20261111.img").write_bytes(b"a" * 1024)
            r = MOD.audit(f, gpt)
            self.assertEqual(r.found, {"boot"})
            self.assertEqual(r.variants, 2)

    def test_overlapping_gpt_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d)
            path = csv_source(f)
            data = path.read_text(encoding="utf-8").replace("2,modem,102,104", "2,modem,101,104")
            path.write_text(data, encoding="utf-8")
            with self.assertRaises(ValueError):
                MOD.load_gpt(path)

    def test_gpt_42_from_repository(self):
        table = MOD.load_gpt(MOD.DEFAULT_GPT)
        self.assertEqual(len(table), 42)
        self.assertEqual(table["boot"], 33554432)
        self.assertEqual(table["userdata"], 5440510464)


if __name__ == "__main__":
    unittest.main()
