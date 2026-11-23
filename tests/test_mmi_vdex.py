"""Synthetic tests; no OEM VDEX included or required."""
import struct
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools' if (ROOT / 'tools').is_dir() else ROOT))
from inspect_mmi_vdex import vdex_sections, quickening_for_method, FormatError


def sample_vdex():
    dex = bytearray(112)
    dex[:8] = b'dex\n037\x00'
    struct.pack_into('<I', dex, 32, len(dex))
    blob = struct.pack('<IHH', 4, 44, 55)
    table_off = len(blob)
    blob += struct.pack('<II', 60, 0)
    blob += struct.pack('<I', table_off)
    # 24 header + 4 checksum + 112 DEX + 0 dependencies + 20 quick data.
    header = b'vdex010\x00' + struct.pack('<IIII', 1, len(dex), 0, len(blob))
    return header + struct.pack('<I', 0) + dex + blob


class Vdex10Tests(unittest.TestCase):
    def test_parse_single_dex(self):
        dex, quick = vdex_sections(sample_vdex())
        self.assertEqual(dex[:8], b'dex\n037\x00')
        self.assertEqual(quickening_for_method(quick, 60), [44,55])

    def test_bad_magic(self):
        invalid = b'abcd' + sample_vdex()[4:]
        with self.assertRaises(FormatError):
            vdex_sections(invalid)

    def test_truncated(self):
        with self.assertRaises(FormatError):
            vdex_sections(sample_vdex()[:-1])

    def test_unknown_method(self):
        _, quick = vdex_sections(sample_vdex())
        with self.assertRaises(FormatError):
            quickening_for_method(quick, 61)

    def test_malformed_table_pointer(self):
        _, quick = vdex_sections(sample_vdex())
        blob = bytearray(quick)
        struct.pack_into('<I', blob, len(blob)-4, 65535)
        with self.assertRaises(FormatError):
            quickening_for_method(blob, 60)


if __name__ == '__main__':
    unittest.main()
