import unittest,json,tempfile,shutil,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'scripts'))
from build_source_worklist import check,build
class SourceWorkTests(unittest.TestCase):
 def test_replay(self):check(ROOT)
 def test_every_record_has_work(self):
  d=build(ROOT);r=json.loads((ROOT/'data/reference/records.json').read_text())
  self.assertEqual([x['record_id'] for x in d['record_work']],[x['record_id'] for x in r]);self.assertTrue(all(not x['admitted'] and not x['primary_edition_verified'] for x in d['record_work']))
 def test_wrong_capture_rejected(self):
  with tempfile.TemporaryDirectory() as t:
   root=Path(t);shutil.copytree(ROOT/'research',root/'research');shutil.copytree(ROOT/'data',root/'data')
   p=root/'research/source-checks.json';d=json.loads(p.read_text());r=json.loads((root/'data/reference/records.json').read_text())[0]
   d['checks'].append({'check_id':'BAD','source_pointer':r['lines'][0]['source_pointer'],'captured_reading':'INVENTED'});p.write_text(json.dumps(d))
   with self.assertRaisesRegex(ValueError,'frozen source'):build(root)
 def test_unknown_line_rejected(self):
  with tempfile.TemporaryDirectory() as t:
   root=Path(t);shutil.copytree(ROOT/'research',root/'research');shutil.copytree(ROOT/'data',root/'data')
   p=root/'research/source-checks.json';d=json.loads(p.read_text());d['checks'].append({'check_id':'BAD','line_questions':[{'source_pointer':'/invented/99'}]});p.write_text(json.dumps(d))
   with self.assertRaisesRegex(ValueError,'unknown line'):build(root)

 def test_additional_publication_omission_rejected(self):
  with tempfile.TemporaryDirectory() as t:
   root=Path(t);shutil.copytree(ROOT/'research',root/'research');shutil.copytree(ROOT/'data',root/'data')
   p=root/'research/publication-reconciliation.json';d=json.loads(p.read_text());d['additional_publications'][0]['entries'].pop();p.write_text(json.dumps(d))
   with self.assertRaisesRegex(ValueError,'publication inventory'):build(root)
 def test_additional_publication_admission_rejected(self):
  with tempfile.TemporaryDirectory() as t:
   root=Path(t);shutil.copytree(ROOT/'research',root/'research');shutil.copytree(ROOT/'data',root/'data')
   p=root/'research/publication-reconciliation.json';d=json.loads(p.read_text());d['additional_publications'][0]['entries'][0]['canonical_admission']=True;p.write_text(json.dumps(d))
   with self.assertRaisesRegex(ValueError,'unsupported publication'):build(root)
