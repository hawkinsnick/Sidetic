import importlib.util,json,tempfile,shutil,unittest
from pathlib import Path
from xml.etree import ElementTree as ET
ROOT=Path(__file__).resolve().parents[1];s=importlib.util.spec_from_file_location('interchange',ROOT/'scripts/build_interchange.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class ReferenceTests(unittest.TestCase):
 def test_every_native_field_roundtrips(self):
  m.replay();self.assertEqual(m.decode((ROOT/m.OUTPUTS[0]).read_bytes()),json.loads((ROOT/'data/reference/records.json').read_bytes()))
 def test_visible_reading_tamper_rejected(self):
  x=ET.fromstring((ROOT/m.OUTPUTS[0]).read_bytes());x.find('.//{'+m.TEI+'}ab').text='invented';
  with self.assertRaisesRegex(ValueError,'source lines'):m.decode(ET.tostring(x))
 def test_payload_loss_rejected(self):
  x=ET.fromstring((ROOT/m.OUTPUTS[0]).read_bytes());part=x.find('.//{'+m.TEI+'}div[@subtype="digital-source-record"]');part.remove(part.find('{'+m.TEI+'}note'))
  with self.assertRaisesRegex(ValueError,'payload'):m.decode(ET.tostring(x))
 def test_source_row_label_tamper_rejected(self):
  x=ET.fromstring((ROOT/m.OUTPUTS[0]).read_bytes());x.find('.//{'+m.TEI+'}ab').set('n','invented')
  with self.assertRaisesRegex(ValueError,'labels'):m.decode(ET.tostring(x))
 def test_source_rights_or_review_promotion_rejected(self):
  with tempfile.TemporaryDirectory() as td:
   root=Path(td)/'repo';shutil.copytree(ROOT,root,ignore=shutil.ignore_patterns('.git','__pycache__'));p=root/'data/reference/records.json';raw=p.read_bytes()
   for key,value in [('source_license','CC-BY-NC-4.0'),('primary_edition_verified',True),('independent_review',True),('physical_object_id','invented')]:
    rows=json.loads(raw);rows[0][key]=value;p.write_text(json.dumps(rows))
    with self.assertRaisesRegex(ValueError,'promotion'):m.build(root)
if __name__=='__main__':unittest.main()
