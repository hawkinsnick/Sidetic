import importlib.util,json,shutil,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('bundle_validator',ROOT/'ai-skill/scripts/validate_bundle.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
class AIIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)/'repo';shutil.copytree(ROOT,self.root,ignore=shutil.ignore_patterns('.git','__pycache__'))
    def tearDown(self):self.tmp.cleanup()
    def test_authorities_validate(self):self.assertTrue(mod.validate(self.root))
    def test_changed_evidence_is_stale(self):
        p=self.root/'data/reference/records.json';p.write_text(p.read_text()+'\n');self.assertRaises(ValueError,mod.validate,self.root)
    def test_missing_authority_fails(self):
        p=self.root/'ai-skill/generated/research-bundle-index.json';d=json.loads(p.read_text());d['artifacts']=d['artifacts'][1:];p.write_text(json.dumps(d));self.assertRaises(ValueError,mod.validate,self.root)
    def test_version_mismatch_fails(self):
        p=self.root/'ai-skill/manifest.json';d=json.loads(p.read_text());d['skill_version']='99';p.write_text(json.dumps(d));self.assertRaises(ValueError,mod.validate,self.root)
if __name__=='__main__':unittest.main()
