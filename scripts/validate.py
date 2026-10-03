"""Validate native source/replay/rights gates; this is not scholarly review."""
import json,sys
from pathlib import Path
from build_reference import write_or_check
ROOT=Path(__file__).resolve().parents[1]
def validate(root=ROOT):
    write_or_check(root)
    from build_governance import check
    check(root)
    from build_source_worklist import check as check_worklist
    check_worklist(root)
    from build_review import check as check_review
    check_review(root)
    status=json.loads((root/'analysis/current-status.json').read_text())
    if status['missing_document_ids']: raise ValueError('incomplete snapshot acquisition')
    if status['verified_primary_edition_readings']!=0 or status['verified_physical_objects']!=0 or status['independent_review']: raise ValueError('unsupported verification claim')
    for f in ['LICENSE','LICENSE-CODE','LICENSE-CONTENT.md','LICENSING.md','NOTICE','DATA-LICENSE-MATRIX.md','research/rights-evidence.json']:
        if not (root/f).is_file(): raise ValueError('missing rights artifact '+f)
    rights=json.loads((root/'research/rights-evidence.json').read_text())
    if rights['license']!='CC-BY-SA-4.0': raise ValueError('source rights mismatch')
    if 'CC BY-SA 4.0' not in (root/'NOTICE').read_text(): raise ValueError('upstream attribution absent')
    records=json.loads((root/'data/reference/records.json').read_text())
    if any(r['source_license']!='CC-BY-SA-4.0' for r in records):raise ValueError('upstream records relicensed')
    if len({r['record_id'] for r in records})!=len(records):raise ValueError('duplicate record IDs')
    return status
if __name__=='__main__':
    try:
        s=validate();print(f"Native integrity PASS: {s['acquired_document_ids']} document IDs; {s['nonempty_source_lines']} source lines; 0 independently verified objects")
    except (ValueError,KeyError) as e: print(e);sys.exit(1)
