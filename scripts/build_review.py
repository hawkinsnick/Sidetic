"""Build a source-bound expert handoff; no review or admission is fabricated."""
import argparse, hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
INPUTS=['data/reference/records.json','analysis/record-admission.json','research/edition-dependencies.json','research/admission-policy.json','research/source-issues.json','research/source-checks.json','research/source-access.json','research/source-worklist.json','research/publication-reconciliation.json','scripts/build_source_worklist.py','research/rights-evidence.json','DATA-LICENSE-MATRIX.md','NOTICE','project.json','scripts/build_review.py','scripts/validate_review.py']
DIMENSIONS=['object_identity','edition_reading','uncertainty','classification','redistribution_rights']
def dump(x):return json.dumps(x,ensure_ascii=False,indent=2)+'\n'
def fingerprint(root):
    entries=[{'path':p,'sha256':hashlib.sha256((root/p).read_bytes()).hexdigest()} for p in INPUTS]
    return hashlib.sha256(json.dumps(entries,sort_keys=True,separators=(',',':')).encode()).hexdigest(),entries
def build(root=ROOT):
    fingerprint_value,inputs=fingerprint(root)
    records=json.loads((root/'data/reference/records.json').read_text());audit=json.loads((root/'analysis/record-admission.json').read_text());checks=json.loads((root/'research/source-checks.json').read_text())['checks']
    if len(records)!=len(audit):raise ValueError("admission coverage mismatch")
    ids={r["record_id"] for r in records}
    if len(ids)!=len(records):raise ValueError("duplicate record IDs")
    check_ids=set()
    for c in checks:
        if c["check_id"] in check_ids:raise ValueError("duplicate source check")
        check_ids.add(c["check_id"])
        if set(c["record_ids"])-ids:raise ValueError("source check references unknown record")
        if c.get("canonical_change") is not False or not c.get("locators"):raise ValueError("source check cannot admit evidence or omit locators")
    packets=[]
    for r,a in zip(records,audit):
        if r['record_id']!=a['record_id']:raise ValueError('admission order mismatch')
        related=[c['check_id'] for c in checks if r['record_id'] in c['record_ids']]
        packets.append({'record_id':r['record_id'],'evidence_fingerprint':fingerprint_value,'record_sha256':hashlib.sha256(dump(r).encode()).hexdigest(),'source_catalog_label':r['source_catalog_label'],'source_headings':r['source_headings'],'source_url':r['source_url'],'source_response_path':r['source_response_path'],'source_row_pointers':[x['source_pointer'] for x in r['lines']],'edition_citations_verbatim':r['references'],'source_checks':related,'priority':'TARGETED_SOURCE_CONFLICT' if related else ('EDITION_LOCATOR_MISSING' if not r['references'] else 'BASELINE_COLLATION'),'blocked_reasons':a['blocked_reasons'],'review_dimensions':DIMENSIONS,'review_status':'NOT_REVIEWED'})
    template={'schema_version':'1.0','evidence_fingerprint':fingerprint_value,'reviewer':{'name':'','expertise':'','independence_statement':''},'reviewed_on':'','decisions':[]}
    summary={'schema_version':'1.0','evidence_fingerprint':fingerprint_value,'input_fingerprints':inputs,'packet_count':len(packets),'source_checked_records':sum(bool(x['source_checks']) for x in packets),'independently_reviewed_records':0,'admitted_records':0,'handoff_status':'PREPARED_FOR_RECORD_LEVEL_REVIEW; SOURCE_ACQUISITION_AND_COLLATION_STILL_INCOMPLETE','review_is_not_automatic_admission':True}
    outputs={'review/packets.json':dump(packets),'review/decision-template.json':dump(template),'review/handoff-manifest.json':dump(summary)}
    index=['# Record review directory','','Choose a record below. Read the [review guide](../docs/EXPERT-REVIEW.md) for the decision process. All packets are pending review.','','| Record | Source label | Priority |','|---|---|---|']
    for r,packet in zip(records,packets):
        filename=r['record_id'].replace(':','-')+'.md'
        label=r['source_catalog_label'].replace('|','\\|')
        index.append(f"| [{r['record_id']}](records/{filename}) | {label} | {packet['priority']} |")
        lines=[f"# Review {r['record_id']}",'',f"Source label: {r['source_catalog_label']}",'','Status: **NOT REVIEWED. Analytical admission remains blocked.**','',f"Record SHA-256: `{packet['record_sha256']}`",f"Evidence fingerprint: `{fingerprint_value}`",'','## Captured source evidence','',f"[eDiAna source]({r['source_url']}); pinned response: `{r['source_response_path']}`. These are digital source transcriptions, not readings independently verified against the object.",'']
        for line in r['lines']:
            lines.extend([f"Source row {line['source_row_label']}; JSON pointer:",'',line['source_pointer'],'','````text',line['reading'],'````',''])
        lines.extend(['## Edition citations as captured',''])
        lines.extend(['- '+ref for ref in r['references']] or ['No edition citations attached to this captured record. Corpus-wide baseline references do not establish record-specific locators.'])
        lines.extend(['','## Source checks and unresolved questions',''])
        related=[c for c in checks if c['check_id'] in packet['source_checks']]
        for c in related:
            lines.extend([f"### {c['check_id']}",'',f"Source: [{c['source_url']}]({c['source_url']})",'', 'Locators: '+'; '.join(c['locators']),'',c['finding'],''])
            if 'proposed_reading' in c:lines.extend(['Attributed scholarly proposal for '+c['proposal_scope']+':','', '````text',c['proposed_reading'],'````',''])
            lines.extend(['- '+q for q in c.get('expert_questions',[])])
            lines.append('')
        if not related:lines.extend(['No targeted source inspection has yet been linked to this record. Consult the edition citations and [source access log](../../research/source-access.json).',''])
        lines.extend(['## Record a decision','','Assess object identity, edition reading, uncertainty, classification and redistribution rights separately. Use the [decision template](../decision-template.json) and [review guide](../../docs/EXPERT-REVIEW.md). Include the record hash and evidence fingerprint above. Review structure checks do not establish expert qualifications or automatically change canonical admission.','','Captured eDiAna evidence retains CC BY-SA 4.0. [Attribution and source rights](../../NOTICE). Linked editions and figures have their own permissions; do not assume rights from public access.',''])
        outputs['review/records/'+filename]='\n'.join(lines)
    outputs['review/README.md']='\n'.join(index)+'\n'
    return outputs
def check(root=ROOT,write=False):
    for p,content in build(root).items():
        path=root/p
        if write:path.parent.mkdir(parents=True,exist_ok=True);path.write_text(content)
        elif not path.exists() or path.read_text()!=content:raise ValueError('stale handoff '+p)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args();check(write=a.write);print('Review handoff replay PASS')
