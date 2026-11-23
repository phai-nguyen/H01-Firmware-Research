"""Synthetic tests only: never require or upload vendor APKs."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from compare_glocalmehome_2846 import sha256_bytes, normalized_method_signature, compare_results


class ComparisonTests(unittest.TestCase):
    def test_digest_deterministic(self):
        a = normalized_method_signature([(0x1a, '2846'), (0x6e, 'Ljava/lang/String;->equals')])
        b = normalized_method_signature([(0x1a, '2846'), (0x6e, 'Ljava/lang/String;->equals')])
        self.assertEqual(a, b)

    def test_changed_reference(self):
        self.assertNotEqual(normalized_method_signature([(0x1a, '2846')]),
                            normalized_method_signature([(0x1a, '1234')]))

    def test_changed_opcode(self):
        self.assertNotEqual(normalized_method_signature([(0x1a, '2846')]),
                            normalized_method_signature([(0x1b, '2846')]))

    def test_sha256_known(self):
        self.assertEqual(sha256_bytes(b'abc'),
                         'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad')

    def test_content_identity_vs_method_identity(self):
        a = {'apk_sha256':'a','dex_sha256':{'classes.dex':'a'},
             'layout_sha256':{'res/layout/assistant_activity.xml':'a'},
             'methods':{'callback':{'instruction_count':2,'digest':'same'}}}
        b = {'apk_sha256':'b','dex_sha256':{'classes.dex':'b'},
             'layout_sha256':{'res/layout/assistant_activity.xml':'b'},
             'methods':{'callback':{'instruction_count':2,'digest':'same'}}}
        c = compare_results(a,b)
        self.assertFalse(c['identical_apk'])
        self.assertTrue(c['methods_semantically_matching']['callback'])
        self.assertFalse(c['dex_byte_identical']['classes.dex'])

    def test_missing_method_is_difference(self):
        a = {'apk_sha256':'a','dex_sha256':{},'layout_sha256':{},'methods':{'x':1}}
        b = {'apk_sha256':'b','dex_sha256':{},'layout_sha256':{},'methods':{}}
        self.assertFalse(compare_results(a,b)['methods_semantically_matching']['x'])


if __name__ == '__main__':
    unittest.main()
