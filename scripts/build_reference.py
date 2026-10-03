"""Replay a source-attributed digital reference corpus; never adjudicate an edition."""
import argparse, hashlib, json, re
from html.parser import HTMLParser
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def dump(value): return json.dumps(value,ensure_ascii=False,indent=2)+'\n'
class Catalog(HTMLParser):
    def __init__(self,language): super().__init__(); self.language=language; self.rows=[]; self.active=None
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if tag=='span' and attrs.get('langid')==self.language:
            if self.active is not None: raise ValueError('nested catalog span')
            self.active=[attrs['docid'],'']
    def handle_data(self,data):
        if self.active is not None: self.active[1]+=data
    def handle_endtag(self,tag):
        if tag=='span' and self.active is not None: self.rows.append(tuple(self.active)); self.active=None

def build(root=ROOT):
    project=json.loads((root/'project.json').read_text())
    base=root/'data/upstream/ediana'
    parser=Catalog(project['language_key']); parser.feed((base/'catalog-fragment.html').read_text())
    catalog=dict(parser.rows)
    if len(catalog)!=len(parser.rows) or not catalog: raise ValueError('empty or duplicate catalog IDs')
    raw=json.loads((base/'response.json').read_text())
    by_id={}
    for title,rows in raw.items():
        if not isinstance(rows,list): raise ValueError('invalid source group')
        for index,row in enumerate(rows):
            did=str(row['docid'])
            if did not in catalog: raise ValueError('unexpected source document '+did)
            escaped=title.replace('~','~0').replace('/','~1')
            by_id.setdefault(did,[]).append((title,index,'/'+escaped+'/'+str(index),row))
    records=[]
    for did,label in catalog.items():
        rows=by_id.get(did,[])
        lines=[]; headings=[]; refs=[]
        for title,index,pointer,row in rows:
            sentence=row.get('sentence')
            if sentence is not None and not isinstance(sentence,str): raise ValueError('non-text sentence')
            if sentence:
                lines.append({'source_row_label':row.get('word'),'reading':sentence,'source_pointer':pointer})
            elif row.get('word'): headings.append(row['word'])
            for ref in row.get('ref') or []:
                if ref not in refs: refs.append(ref)
        records.append({'record_id':project['language_key']+':ediana:'+did,'source_document_id':did,'source_catalog_label':label,'source_response_groups':list(dict.fromkeys(x[0] for x in rows)),'source_headings':headings,'lines':lines,'references':refs,'source_url':'https://www.ediana.gwi.uni-muenchen.de/corpus.php','source_response_path':'data/upstream/ediana/response.json','source_license':'CC-BY-SA-4.0','evidence_layer':'digital_reference','primary_edition_verified':False,'physical_object_id':None,'independent_review':False,'acquisition_state':'ACQUIRED' if rows else 'MISSING'})
    labels={}
    for did,label in catalog.items(): labels.setdefault(label,[]).append(did)
    collisions=[{'catalog_label':k,'document_ids':v,'resolution':'UNRESOLVED; preserve distinct source IDs and headings'} for k,v in labels.items() if len(v)>1]
    missing=[did for did in catalog if did not in by_id]
    status={'schema_version':'1.0','project':project['name'],'version':project['version'],'stage':'SOURCE_ATTRIBUTED_DIGITAL_REFERENCE','source_version':project['source_version'],'snapshot_date':'2026-10-03','directory_document_ids':len(catalog),'response_group_titles':len(raw),'acquired_document_ids':len(by_id),'missing_document_ids':missing,'nonempty_source_lines':sum(len(x['lines']) for x in records),'verified_primary_edition_readings':0,'verified_physical_objects':0,'independent_review':False,'analytical_admission':'BLOCKED_PENDING_EDITION_AND_OBJECT_RECONCILIATION','coverage_scope':'captured eDiAna directory; not a claim of language-wide completeness','catalog_label_collisions':collisions,'source_fingerprints':{'catalog-fragment.html':digest(base/'catalog-fragment.html'),'response.json':digest(base/'response.json')},'source_license':'CC-BY-SA-4.0'}
    return {'data/reference/records.json':dump(records),'analysis/current-status.json':dump(status)}

def write_or_check(root=ROOT,write=False):
    outputs=build(root)
    for path,content in outputs.items():
        p=root/path
        if write: p.parent.mkdir(parents=True,exist_ok=True);p.write_text(content)
        elif not p.is_file() or p.read_text()!=content: raise ValueError('stale derived file '+path)
    return outputs
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args()
    write_or_check(write=args.write)
    print('Source-attributed reference replay PASS')
