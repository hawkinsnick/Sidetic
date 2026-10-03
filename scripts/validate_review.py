"""Validate a submitted review against pinned evidence; never update canonical admission."""
import argparse, json, re
from pathlib import Path
from datetime import date
from build_review import ROOT, fingerprint, DIMENSIONS, check
STATES={'SUPPORTED','DISPUTED','INSUFFICIENT_EVIDENCE','NOT_ASSESSED'}
def validate_review(review,root=ROOT):
    check(root)
    current,_=fingerprint(root)
    if review.get('schema_version')!='1.0' or review.get('evidence_fingerprint')!=current:raise ValueError('review evidence revision mismatch')
    reviewer=review.get('reviewer',{})
    if any(not isinstance(reviewer.get(k),str) or not reviewer[k].strip() for k in ['name','expertise','independence_statement']):raise ValueError('reviewer identity, expertise and independence required')
    try:reviewed=date.fromisoformat(review['reviewed_on'])
    except (ValueError,KeyError,TypeError):raise ValueError('valid review date required')
    if reviewed>date.today():raise ValueError('future review date')
    decisions=review.get('decisions')
    if not isinstance(decisions,list) or not decisions:raise ValueError('review decisions required')
    packets={x['record_id']:x for x in json.loads((root/'review/packets.json').read_text())};seen=set()
    for d in decisions:
        rid=d.get('record_id');dimension=d.get('dimension');key=(rid,dimension)
        if rid not in packets or dimension not in DIMENSIONS:raise ValueError('unknown record or dimension')
        if key in seen:raise ValueError('duplicate record dimension decision')
        seen.add(key)
        if d.get('record_sha256')!=packets[rid]['record_sha256']:raise ValueError('record evidence mismatch')
        if d.get('state') not in STATES:raise ValueError('unknown decision state')
        if not isinstance(d.get('rationale'),str) or not d['rationale'].strip():raise ValueError('decision rationale required')
        citations=d.get('evidence_citations')
        if not isinstance(citations,list):raise ValueError('evidence citations must be a list')
        if d['state'] in {'SUPPORTED','DISPUTED'} and not citations:raise ValueError('substantive decision requires evidence citations')
        for c in citations:
            if not isinstance(c,dict) or not isinstance(c.get('source'),str) or not c['source'].strip() or not isinstance(c.get('locator'),str) or not c['locator'].strip():raise ValueError('source and precise locator required')
        if d.get('canonical_admission',False) is not False:raise ValueError('review cannot auto-admit canonical evidence')
    return {'status':'REVIEW_STRUCTURE_VALID','decisions':len(decisions),'canonical_admission':False,'limitation':'Structure and revision checked; expertise and scientific correctness not independently authenticated'}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('review_json');a=p.parse_args();print(json.dumps(validate_review(json.loads(Path(a.review_json).read_text())),indent=2))
