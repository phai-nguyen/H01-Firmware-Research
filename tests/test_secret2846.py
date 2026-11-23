"""Verify public MMI documentation retains evidence distinctions and table counts."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class Secret2846Tests(unittest.TestCase):
    def test_documentation_keeps_uncertainty(self):
        doc = (ROOT / 'docs/system/glocalmehome-about-secret-code-2846.md').read_text('utf-8')
        self.assertIn('MySecretCodeReceiver', doc)
        self.assertIn('2846', doc)
        self.assertIn('CHƯA', doc)
        self.assertIn('onReceive()', doc)

    def test_mmi_inventory_counts(self):
        doc = (ROOT / 'docs/system/mmi-factory-tests.md').read_text('utf-8')
        rows = [line for line in doc.splitlines() if line.startswith('| ') and
                line.split('|')[1].strip().isdigit()]
        self.assertEqual(len(rows), 30)
        cells = [[x.strip() for x in row.strip('|').split('|')] for row in rows]
        self.assertEqual(sum(row[2] == 'T' for row in cells), 20)
        self.assertEqual(sum(row[3] == 'T' for row in cells), 10)

if __name__ == '__main__':
    unittest.main()
