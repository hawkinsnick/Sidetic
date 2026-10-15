"""Block invented consultation, stale native data and unsupported promotions."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
from source_collation import Collation, ROOT, PACKET, REPORT, PDF


class SourceCollationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.data = json.loads((ROOT/PACKET).read_text())
        paths = [PACKET, 'scripts/source_collation.py'] + [r['path'] for r in self.data['inputs']]
        for path in paths:
            p = self.root/path
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes((ROOT/path).read_bytes())

    def save(self):
        (self.root/PACKET).write_text(json.dumps(self.data))

    def test_recorded_report(self):
        self.assertEqual(Collation().report(), json.loads((ROOT/REPORT).read_text()))

    def test_native_identity_and_modalities_preserved(self):
        r = Collation(self.root)
        for key in r.cases:
            c = r.case(key)
            self.assertEqual(c['native_evidence'].get('check_id', c['native_evidence'].get('comparison_id')), key)
            self.assertTrue(all(s['limits'] for s in c['sources']))

    def test_any_stale_input_blocks_queries(self):
        p = self.root/self.data['inputs'][-1]['path']
        p.write_text(p.read_text()+'\n')
        with self.assertRaisesRegex(ValueError, 'stale collation'):
            Collation(self.root)

    def test_cannot_turn_bibliography_or_web_into_visual_review(self):
        s = self.data['sources'][0]
        s['consultation'] = PDF
        s['source_pdf_sha256'] = None
        self.save()
        with self.assertRaisesRegex(ValueError, 'lacks receipt'):
            Collation(self.root)

    def test_uncertainty_and_work_not_implicitly_closed(self):
        self.data['cases'][0]['remaining_work'] = []
        self.save()
        with self.assertRaises(ValueError):
            Collation(self.root)

    def test_no_scholarly_promotion(self):
        self.data['cases'][0]['new_canonical_reading'] = True
        self.save()
        with self.assertRaisesRegex(ValueError, 'promotion'):
            Collation(self.root)

    def test_changed_native_locus_rejected(self):
        self.data['cases'][0]['native_evidence']['pointer'] = '/invented-locus'
        self.save()
        with self.assertRaises((KeyError, ValueError)):
            Collation(self.root)

    def test_wrong_local_pdf_rejected(self):
        r = Collation(self.root)
        source = next(s['source_id'] for s in self.data['sources'] if s['consultation']==PDF)
        p = self.root/'fake.pdf'
        p.write_bytes(b'%PDF-fake')
        with self.assertRaisesRegex(ValueError, 'bytes differ'):
            r.verify_source(source, p)

    def test_duplicate_case_rejected(self):
        self.data['cases'].append(copy.deepcopy(self.data['cases'][0]))
        self.save()
        with self.assertRaises(ValueError):
            Collation(self.root)

    def test_corpus_specific_critical_boundary(self):
        d = {c['review_id']:c['details'] for c in self.data['cases']}
        name = self.data['repository'].split('/')[-1]
        if name == 'Cypro-Minoan':
            r = d['CM209-aii501-internal-comparison']
            self.assertEqual((r['position'],r['table_label'],r['critical_reedition_label']), (2,'09','10'))
            self.assertEqual(r['nearby_discussion_position'],4)
            self.assertFalse(r['encoded_occurrence_added'])
        elif name == 'Sidetic':
            r = d['SID-EUEMPOLOS-2025']
            self.assertEqual(r['source_printed_form'],'ewpel')
            self.assertFalse(r['previous_underdots_are_source_typography'])
            native = Collation().case('SID-EUEMPOLOS-2025')['native_evidence']
            self.assertEqual(native['proposed_reading'],'ewpel')
            self.assertEqual(native['superseded_project_representation'],r['previous_project_form'])
        elif name == 'Pisidian':
            self.assertEqual(d['PIS-N24-2023']['line_count_in_edition'],2)
            self.assertEqual(d['PIS-ADIEGO2012-N37']['limited_restoration_fragment'],'[Tas?]')
            self.assertFalse(d['PIS-KESME2-AMBIGUITIES']['segmentation_is_observed_spacing'])
        elif name == 'Lydian':
            self.assertFalse(d['LYD-LW40-2016']['full_line_typography_verified'])
            self.assertEqual(d['LYD-GUSMANI1975-LW59']['source_printed_ambiguity'],['d','v'])


if __name__ == '__main__':
    unittest.main()
