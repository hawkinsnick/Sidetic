"""Check a bounded source-collation packet; integrity is not scholarly acceptance."""
import argparse
from collections import Counter
import hashlib
import json
import re
from pathlib import Path
from evidence_query import local, pointer

ROOT = Path(__file__).resolve().parents[1]
PACKET = 'research/source-collation-2026-10-15.json'
REPORT = 'analysis/source-collation-2026-10-15.json'
PDF = 'DIRECT_RENDERED_PDF_PAGE_IMAGES'
MODES = {PDF, 'BIBLIOGRAPHIC_ROUTE_ONLY', 'DIRECT_AUTHOR_POSTED_WEB_TEXT_PAGE_MARKERS',
         'DIRECT_PUBLISHER_PROVIDED_WEB_TEXT_PAGE_MARKERS'}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def valid_sha(value):
    return isinstance(value, str) and bool(re.fullmatch('[0-9a-f]{64}', value))


class Collation:
    def __init__(self, root=ROOT):
        self.root = Path(root)
        raw = local(self.root, PACKET).read_bytes()
        self.packet_sha = sha(raw)
        self.data = d = json.loads(raw)
        if d['format'] != 'corpus-source-collation-v1':
            raise ValueError('invalid collation format')
        if d['accepted_readings_added'] != 0 or d['independent_reviews_added'] != 0 or d['frozen_readings_changed'] is not False or d['source_files_redistributed'] is not False:
            raise ValueError('unsupported promotion or redistribution')
        self.inputs = {}
        for r in d['inputs']:
            if r['path'] in self.inputs:
                raise ValueError('duplicate input')
            b = local(self.root, r['path']).read_bytes()
            if sha(b) != r['sha256']:
                raise ValueError('stale collation evidence: ' + r['path'])
            self.inputs[r['path']] = json.loads(b)
        if d['frozen_readings_input'] not in self.inputs:
            raise ValueError('frozen input not pinned')
        self.sources = {}
        for s in d['sources']:
            key = s['source_id']
            if key in self.sources or s['consultation'] not in MODES or not s['citation'] or not s['url'] or not s['limits']:
                raise ValueError('invalid source attribution')
            if s['source_file_redistributed'] is not False:
                raise ValueError('source redistribution not authorized')
            if s['consultation'] == PDF:
                if not valid_sha(s['source_pdf_sha256']) or not s['source_pdf_bytes'] or not s['page_inspections']:
                    raise ValueError('PDF consultation lacks receipt')
                for page in s['page_inspections']:
                    if page['pdf_ordinal'] < 1 or not page['printed_locator'] or not valid_sha(page['render_sha256']) or page['render_redistributed'] is not False:
                        raise ValueError('invalid page inspection receipt')
            elif s['source_pdf_sha256'] is not None or s['page_inspections']:
                raise ValueError('non-PDF consultation promoted to PDF')
            if 'WEB_TEXT' in s['consultation'] and not s.get('web_locators'):
                raise ValueError('web consultation lacks locator')
            self.sources[key] = s
        self.cases = {}
        for c in d['cases']:
            key = c['review_id']
            if key in self.cases or not c['observations'] or not c['remaining_work']:
                raise ValueError('invalid or duplicate case')
            if c['new_canonical_reading'] is not False or c['independent_review'] is not False or c['physical_identity_certified'] is not False:
                raise ValueError('unsupported case promotion')
            if not c['source_ids'] or set(c['source_ids']) - self.sources.keys():
                raise ValueError('unknown case source')
            r = c['native_evidence']
            native = pointer(self.inputs[r['path']], r['pointer'])
            if native.get('comparison_id', native.get('check_id')) != key:
                raise ValueError('native case identity mismatch')
            self.cases[key] = c

    def case(self, key):
        c = self.cases[key]
        r = c['native_evidence']
        return {'collation': c, 'native_evidence': pointer(self.inputs[r['path']], r['pointer']),
                'sources': [self.sources[s] for s in c['source_ids']]}

    def verify_source(self, source_id, path):
        s = self.sources[source_id]
        if s['consultation'] != PDF:
            raise ValueError('no directly inspected PDF receipt for this source')
        b = Path(path).read_bytes()
        if not b.startswith(b'%PDF') or sha(b) != s['source_pdf_sha256'] or len(b) != s['source_pdf_bytes']:
            raise ValueError('source bytes differ from inspected PDF')
        return {'source_id':source_id, 'bytes_match':True, 'scholarly_acceptance_granted':False}

    def report(self):
        return {'format':'corpus-source-collation-audit-v1', 'repository':self.data['repository'],
                'status':'PASS_PACKET_INTEGRITY_NOT_EPIGRAPHIC_ADJUDICATION',
                'packet_sha256':self.packet_sha,
                'implementation_sha256':sha((self.root/'scripts/source_collation.py').read_bytes()),
                'comparison_tasks':len(self.cases),
                'source_consultation_modes':dict(sorted(Counter(s['consultation'] for s in self.sources.values()).items())),
                'rendered_page_inspections':sum(len(s['page_inspections']) for s in self.sources.values()),
                'project_representation_corrections':self.data['project_representation_corrections'],
                'frozen_readings_changed':False, 'accepted_readings_added':0,
                'independent_reviews_added':0, 'source_files_redistributed':False,
                'alternative_pair_total':None, 'independent_witness_total':None,
                'literature_exhaustive':False}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    g = p.add_mutually_exclusive_group()
    g.add_argument('--case')
    g.add_argument('--write', action='store_true')
    g.add_argument('--check', action='store_true')
    g.add_argument('--verify-source', nargs=2, metavar=('SOURCE_ID', 'LOCAL_PDF'))
    a = p.parse_args()
    collation = Collation()
    if a.case:
        result = collation.case(a.case)
    elif a.verify_source:
        result = collation.verify_source(*a.verify_source)
    else:
        result = collation.report()
        rendered = json.dumps(result, ensure_ascii=False, indent=2)+'\n'
        if a.write:
            (ROOT/REPORT).write_text(rendered)
        elif a.check and (ROOT/REPORT).read_text() != rendered:
            raise SystemExit('stale collation report')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
