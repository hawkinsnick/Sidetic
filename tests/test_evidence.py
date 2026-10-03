import importlib.util,json,shutil,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
import sys
sys.path.insert(0,str(ROOT/'scripts'))
from build_reference import build,write_or_check
from validate import validate
class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)/'repo'
        shutil.copytree(ROOT,self.root,ignore=shutil.ignore_patterns('.git','__pycache__'))
    def tearDown(self):self.tmp.cleanup()
    def test_committed_replay(self):
        self.assertEqual(build(self.root),build(self.root));write_or_check(self.root);validate(self.root)
    def test_source_change_detected(self):
        p=self.root/'data/upstream/ediana/response.json';d=json.loads(p.read_text())
        row=next(x for rows in d.values() for x in rows if x.get('sentence'));row['sentence']+='[?]'
        p.write_text(json.dumps(d));self.assertRaises(ValueError,write_or_check,self.root)
    def test_uncertainty_preserved(self):
        p=self.root/'data/upstream/ediana/response.json';d=json.loads(p.read_text())
        row=next(x for rows in d.values() for x in rows if x.get('sentence'));row['sentence']='[a?] ḅ—c'
        p.write_text(json.dumps(d));records=json.loads(build(self.root)['data/reference/records.json'])
        self.assertTrue(any(line['reading']=='[a?] ḅ—c' for r in records for line in r['lines']))
    def test_unexpected_source_id_rejected(self):
        p=self.root/'data/upstream/ediana/response.json';d=json.loads(p.read_text());next(iter(d.values()))[0]['docid']='NOT-IN-CATALOG'
        p.write_text(json.dumps(d));self.assertRaises(ValueError,build,self.root)
    def test_missing_source_remains_visible(self):
        p=self.root/'data/upstream/ediana/response.json';d=json.loads(p.read_text());did=next(iter(d.values()))[0]['docid']
        d={k:[r for r in rows if r['docid']!=did] for k,rows in d.items()};p.write_text(json.dumps(d))
        write_or_check(self.root,True);s=json.loads((self.root/'analysis/current-status.json').read_text())
        self.assertIn(str(did),s['missing_document_ids']);self.assertRaises(ValueError,validate,self.root)
    def test_merged_group_keeps_document_identity(self):
        p=self.root/'data/upstream/ediana/response.json';d=json.loads(p.read_text());items=list(d.items());self.assertGreater(len(items),1)
        d[items[0][0]].extend(d.pop(items[1][0]));p.write_text(json.dumps(d))
        before=json.loads(build()['data/reference/records.json']);after=json.loads(build(self.root)['data/reference/records.json'])
        self.assertEqual({x['record_id'] for x in before},{x['record_id'] for x in after})
    def test_upstream_license_cannot_be_overridden(self):
        p=self.root/'research/rights-evidence.json';d=json.loads(p.read_text());d['license']='CC-BY-NC-4.0';p.write_text(json.dumps(d))
        self.assertRaises(ValueError,validate,self.root)
    def test_no_independent_verification_claims(self):
        s=json.loads(build(self.root)['analysis/current-status.json']);self.assertFalse(s['independent_review']);self.assertEqual(s['verified_physical_objects'],0)
if __name__=='__main__':unittest.main()
