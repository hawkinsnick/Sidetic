"""Build reproducible AI evidence fingerprints from native authority files."""
import hashlib,json,os,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def build():
    manifest=json.loads((ROOT/'ai-skill/manifest.json').read_text())
    profile=json.loads((ROOT/'ai-skill/references/authority-profile.json').read_text())
    paths=[(x['role'],x['path']) for x in profile['required_authorities']]+[('raw_source','data/upstream/ediana/response.json'),('source_catalog','data/upstream/ediana/catalog-fragment.html')]
    paths += [('native_evidence_profile', 'research/evidence-query-profile.json'), ('native_evidence_coverage', 'analysis/evidence-query-coverage.json'), ('native_evidence_query', 'scripts/evidence_query.py'), ('native_evidence_query_tests', 'scripts/test_native_evidence_query.py'), ('native_evidence_guide', 'docs/EVIDENCE-AND-ALTERNATIVES.md')]
    paths += [('attribution_review', 'research/attribution-review.json'), ('attribution_review', 'analysis/attribution-review-audit.json'), ('attribution_review', 'docs/ATTRIBUTION-REVIEW.md'), ('attribution_review', 'scripts/attribution_review.py'), ('attribution_review', 'scripts/test_attribution_review.py')]
    paths += [('selected_source_collation', 'research/source-collation-2026-10-15.json'), ('selected_source_collation', 'analysis/source-collation-2026-10-15.json'), ('selected_source_collation', 'docs/SOURCE-COLLATION-2026-10-15.md'), ('selected_source_collation', 'scripts/source_collation.py'), ('selected_source_collation', 'scripts/test_source_collation.py')]
    paths += [('abydos_edition_comparison', 'docs/ABYDOS-EDITION-COMPARISON-2026-10-16.md')]
    paths += [("research_delivery", p) for p in ['scripts/research_delivery.py','scripts/test_research_delivery.py','docs/RESEARCH-DELIVERY.md','analysis/research-delivery.json']]
    artifacts=[]
    for role,path in paths:
        b=(ROOT/path).read_bytes();artifacts.append({'role':role,'path':path,'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)})
    source=os.environ.get('SOURCE_COMMIT') or subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
    fingerprint=hashlib.sha256(json.dumps(artifacts,sort_keys=True).encode()).hexdigest()
    out=ROOT/'ai-skill/generated';out.mkdir(exist_ok=True)
    bundle={'schema_version':'0.3.1','skill_version':manifest['skill_version'],'source_commit':source,'evidence_fingerprint_sha256':fingerprint,'canonical_repository':True,'artifacts':artifacts,'contract':{'corpus_is_authoritative':True,'missing_means_unknown':True,'preserve_uncertainty':True,'preserve_rights':True,'preserve_source_independence':True,'cross_corpus_equivalence_requires_explicit_evidence':True}}
    (out/'research-bundle-index.json').write_text(json.dumps(bundle,indent=2)+'\n')
    (out/'source-state.json').write_text(json.dumps({'schema_version':'1.0','skill_version':manifest['skill_version'],'source_commit':source,'evidence_fingerprint_sha256':fingerprint,'bundle_index':'ai-skill/generated/research-bundle-index.json','commit_semantics':'commit used for bundle generation; subsequent bundle-only commits do not change indexed evidence'},indent=2)+'\n')
    text=(ROOT/'ai-skill/SKILL.md').read_text()+'\n\n'+(ROOT/'ai-skill/references/corpus-project-contract.md').read_text()+'\n\n'+(ROOT/'docs/START-HERE.md').read_text()
    (ROOT/'ai-skill/Research-Starter.txt').write_text(text)
    print('AI evidence bundle built:',fingerprint)
if __name__=='__main__':build()
