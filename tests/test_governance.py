import unittest, tempfile, shutil, sys, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'scripts'))
from build_governance import check, build_governance
class GovernanceTests(unittest.TestCase):
    def clone(self):
        tmp=tempfile.TemporaryDirectory();self.addCleanup(tmp.cleanup);root=Path(tmp.name)/'repo';shutil.copytree(ROOT,root,ignore=shutil.ignore_patterns('.git','__pycache__'));return root
    def test_committed_audit_replays(self): check(ROOT)
    def test_raw_tampering_cannot_be_legitimized_by_rebuild(self):
        root=self.clone();p=root/'data/upstream/ediana/response.json';p.write_bytes(p.read_bytes()+b' ')
        with self.assertRaisesRegex(ValueError,'snapshot hash'): build_governance(root)
    def test_false_admission_is_rejected(self):
        root=self.clone();p=root/'analysis/record-admission.json';x=json.loads(p.read_text());x[0]['analytical_admission']=True;p.write_text(json.dumps(x))
        with self.assertRaisesRegex(ValueError,'stale governance'):check(root)
    def test_wrong_acquisition_scope_is_rejected(self):
        root=self.clone();p=root/'research/acquisition.json';x=json.loads(p.read_text());x['request_fields']['docids']+='999999';p.write_text(json.dumps(x))
        with self.assertRaisesRegex(ValueError,'request'):build_governance(root)
    def test_marker_absence_never_means_certainty(self):
        x=json.loads(build_governance(ROOT)['analysis/record-admission.json']);self.assertTrue(all(l['epigraphic_certainty']=='NOT_ADJUDICATED' for r in x for l in r['lines']))
