"""Synthetic tests only: no OEM firmware required."""
from pathlib import Path
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from inspect_assistant_routes import ordered_symbols, ROUTES

class AssistantRoutesTest(unittest.TestCase):
    def test_known_routes_count(self):
        self.assertEqual(len(ROUTES), 3)

    def test_ordered_match(self):
        refs = [(0x1a,'package'),(0x6e,'check'),(0x28,None),(0x6e,'launch')]
        self.assertTrue(ordered_symbols(refs, ['package','check','launch']))

    def test_wrong_order_rejected(self):
        self.assertFalse(ordered_symbols([(1,'launch'),(1,'check')], ['check','launch']))

    def test_missing_target_rejected(self):
        self.assertFalse(ordered_symbols([(1,'a'),(1,'b')], ['a','c']))

    def test_repetition_matters(self):
        self.assertFalse(ordered_symbols([(1,'pkg'),(2,'setClass')], ['pkg','pkg','setClass']))

    def test_routes_are_disjoint(self):
        targets = {(data[1],data[2]) for data in ROUTES.values()}
        self.assertEqual(len(targets),3)

if __name__ == '__main__': unittest.main()
