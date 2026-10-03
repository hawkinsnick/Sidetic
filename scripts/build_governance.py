"""Deterministic governance audit; syntactic flags are not epigraphic judgments."""
import json, hashlib, re, argparse
from pathlib import Path
from build_reference import build, Catalog
ROOT=Path(__file__).resolve().parents[1]
def dump(x): return json.dumps(x,ensure_ascii=False,indent=2)+'\n'
def build_governance(root=ROOT):
    p=json.loads((root/'project.json').read_text()); native=build(root)
    records=json.loads(native['data/reference/records.json']); status=json.loads(native['analysis/current-status.json'])
    acquisition=json.loads((root/'research/acquisition.json').read_text())
    raw=root/'data/upstream/ediana/response.json'
    if hashlib.sha256(raw.read_bytes()).hexdigest()!=acquisition['raw_response_sha256']: raise ValueError('snapshot hash disagrees with acquisition record')
    requested=acquisition['request_fields']['docids'].split(',')
    if len(requested)!=len(set(requested)) or set(requested)!={r['source_document_id'] for r in records}: raise ValueError('acquisition request does not match catalog')
    if acquisition['request_fields']['language']!=p['language_key']: raise ValueError('acquisition language mismatch')
    audit=[]; ledger=[]
    for r in records:
        lines=[]
        for line in r['lines']:
            text=line['reading']; flags=[]
            for name,pattern in [('brackets',r'[\[\]⟦⟧]'),('question_mark',r'\?'),('combining_underdot',r'\u0323'),('source_markup',r'<[^>]+>'),('ellipsis',r'\.\.\.|…')]:
                if re.search(pattern,text): flags.append(name)
            lines.append({'source_pointer':line['source_pointer'],'reading_sha256':hashlib.sha256(text.encode()).hexdigest(),'syntactic_flags':flags,'epigraphic_certainty':'NOT_ADJUDICATED'})
        audit.append({'record_id':r['record_id'],'lines':lines,'analytical_admission':False,'blocked_reasons':['PRIMARY_EDITION_NOT_COLLATED','PHYSICAL_OBJECT_NOT_RECONCILED','INDEPENDENT_REVIEW_ABSENT'],'edition_locator_status':'SOURCE_CITATIONS_UNRESOLVED' if r['references'] else 'NO_ROW_EDITION_CITATION'})
        ledger.append({'record_id':r['record_id'],'source_document_id':r['source_document_id'],'catalog_label':r['source_catalog_label'],'source_headings':r['source_headings'],'source_citations_verbatim':r['references'],'citation_join':'UNRESOLVED; bibliographic search results are candidates, not edition equivalences','witness_family':'ediana-digital-snapshot','physical_object_id':None,'independent_witness_count':None})
    benchmark={'repository':{'name':p['name'],'version':p['version']},'status_source':{'path':'analysis/current-status.json','checked':True},'coverage':{'unit':'eDiAna directory document ID','known_total':len(records),'represented':len(records),'admitted':0,'independently_reviewed':0,'scope':status['coverage_scope'],'language_wide_total':None},'rights':{'project_original_policy':'Project code PolyForm Noncommercial; original content CC BY-NC 4.0','third_party_separate':True},'evidence_layers':{'source_observation':'Pinned digital transcription, not autopsy','normalization':'No silently normalized canonical text','computation':'Deterministic syntactic audit only','interpretation':'Source proposals remain attributed hypotheses'},'gates':{'blocked_claims':['decipherment','language-wide completeness','independently verified objects','newly established sign values'],'next_gate':'Edition and physical-object reconciliation, followed by independent epigraphic review'},'ai':{'authority_profile':'ai-skill/references/authority-profile.json','canonical_data_outranks_bundle':True}}
    return {'analysis/record-admission.json':dump(audit),'research/edition-dependencies.json':dump(ledger),'analysis/benchmark-status.json':dump(benchmark)}
def check(root=ROOT,write=False):
    for name,content in build_governance(root).items():
        path=root/name
        if write: path.write_text(content)
        elif not path.exists() or path.read_text()!=content: raise ValueError('stale governance artifact '+name)
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args();check(write=args.write);print('Governance replay PASS')
