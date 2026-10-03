import unittest,json,tempfile,shutil,sys,copy
from pathlib import Path
from datetime import date
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'scripts'))
from build_review import check
from validate_review import validate_review
class ReviewTests(unittest.TestCase):
 def sample(self):
  t=json.loads((ROOT/'review/decision-template.json').read_text());p=json.loads((ROOT/'review/packets.json').read_text())[0]
  t.update(reviewer={'name':'Test fixture reviewer','expertise':'Fixture only','independence_statement':'Not a real review'},reviewed_on=date.today().isoformat(),decisions=[{'record_id':p['record_id'],'record_sha256':p['record_sha256'],'dimension':'edition_reading','state':'INSUFFICIENT_EVIDENCE','rationale':'Fixture tests structure only','evidence_citations':[]}]);return t
 def test_handoff_replays(self):check(ROOT)
 def test_structure_does_not_admit(self):self.assertFalse(validate_review(self.sample())['canonical_admission'])
 def test_old_revision_rejected(self):
  t=self.sample();t['evidence_fingerprint']='0'*64
  with self.assertRaisesRegex(ValueError,'revision'):validate_review(t)
 def test_wrong_record_hash_rejected(self):
  t=self.sample();t['decisions'][0]['record_sha256']='0'*64
  with self.assertRaisesRegex(ValueError,'record evidence'):validate_review(t)
 def test_unsupported_positive_decision_rejected(self):
  t=self.sample();t['decisions'][0]['state']='SUPPORTED'
  with self.assertRaisesRegex(ValueError,'citations'):validate_review(t)
 def test_anonymous_review_rejected(self):
  t=self.sample();t['reviewer']['name']=''
  with self.assertRaisesRegex(ValueError,'reviewer'):validate_review(t)
 def test_review_cannot_auto_admit(self):
  t=self.sample();t['decisions'][0]['canonical_admission']=True
  with self.assertRaisesRegex(ValueError,'auto-admit'):validate_review(t)
 def test_duplicates_rejected(self):
  t=self.sample();t['decisions'].append(copy.deepcopy(t['decisions'][0]))
  with self.assertRaisesRegex(ValueError,'duplicate'):validate_review(t)
