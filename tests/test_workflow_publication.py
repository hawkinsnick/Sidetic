from pathlib import Path
import unittest
ROOT = Path(__file__).resolve().parents[1]
class PublicationWorkflowTests(unittest.TestCase):
    def test_single_guarded_publisher(self):
        workflows = list((ROOT / '.github/workflows').glob('*.yml'))
        text = '\n'.join(p.read_text() for p in workflows)
        self.assertNotIn('git pull --rebase', text)
        self.assertNotIn('git push --force', text)
        self.assertEqual(text.count('python ai-skill/scripts/publish_sync.py'), 1)
        self.assertNotIn('  sync:', (ROOT / '.github/workflows/validate.yml').read_text())
        self.assertIn('python scripts/test_preexpert_parity.py', (ROOT / '.github/workflows/validate.yml').read_text())
