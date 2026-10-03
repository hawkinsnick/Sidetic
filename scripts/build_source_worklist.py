"""Account for every frozen citation and every record requiring source work."""
import argparse,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def dump(x):return json.dumps(x,ensure_ascii=False,indent=2)+'\n'
def build(root=ROOT):
 records=json.loads((root/'data/reference/records.json').read_text())
 checks=json.loads((root/'research/source-checks.json').read_text())['checks']
 pointers={line['source_pointer']:line['reading'] for r in records for line in r['lines']}
 for c in checks:
  if c.get('source_pointer'):
   if c['source_pointer'] not in pointers:raise ValueError('unknown checked source pointer')
   if 'captured_reading' in c and c['captured_reading']!=pointers[c['source_pointer']]:raise ValueError('checked reading differs from frozen source')
  for q in c.get('line_questions',[]):
   if q['source_pointer'] not in pointers:raise ValueError('unknown line question pointer')
 citations=sorted({s for r in records for s in r['references']})
 entries=[{'citation_verbatim':s,'record_ids':[r['record_id'] for r in records if s in r['references']],'join_state':'UNRESOLVED; title, edition and locator must be checked separately','next_action':'Acquire the exact cited edition and collate the indicated passage; do not equate a bibliography search hit with inspected content'} for s in citations]
 work=[{'record_id':r['record_id'],'review_page':'review/records/'+r['record_id'].replace(':','-')+'.md','citations_verbatim':r['references'],'source_check_ids':[c['check_id'] for c in checks if r['record_id'] in c['record_ids']],'remaining_work':['Confirm edition-to-record concordance','Collate every source row, including uncertainty and layout','Reconcile object identity and inventory','Establish applicable reuse rights','Obtain independent expert review'],'primary_edition_verified':False,'physical_object_verified':False,'admitted':False} for r in records]
 return {'schema_version':'1.0','scope':'Frozen digital snapshot; not a language-wide inventory or completeness claim','record_count':len(records),'distinct_citation_count':len(entries),'records_without_captured_citations':[r['record_id'] for r in records if not r['references']],'bibliographic_candidates_path':'data/upstream/ediana/bibliography.json','access_log_path':'research/source-access.json','new_publication_leads_path':'research/source-frontier.json','citation_dependencies':entries,'record_work':work}
def check(root=ROOT,write=False):
 p=root/'research/source-worklist.json';content=dump(build(root))
 if write:p.write_text(content)
 elif not p.exists() or p.read_text()!=content:raise ValueError('stale source worklist')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();check(write=a.write);print('Source worklist replay PASS')
