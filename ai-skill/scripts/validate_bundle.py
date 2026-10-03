import hashlib,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def validate(root=ROOT):
    a=root/'ai-skill';manifest=json.loads((a/'manifest.json').read_text());profile=json.loads((a/'references/authority-profile.json').read_text())
    bundle=json.loads((a/'generated/research-bundle-index.json').read_text());state=json.loads((a/'generated/source-state.json').read_text())
    version=re.search(r'^version:\s*(\S+)',(a/'SKILL.md').read_text(),re.M).group(1)
    if not(version==manifest['skill_version']==bundle['skill_version']==state['skill_version']):raise ValueError('skill version mismatch')
    if not re.fullmatch('[0-9a-f]{40}',bundle['source_commit']):raise ValueError('invalid source commit')
    if state['source_commit']!=bundle['source_commit']:raise ValueError('source commit mismatch')
    paths={x['path'] for x in bundle['artifacts']}
    if not {x['path'] for x in profile['required_authorities']}<=paths:raise ValueError('authority missing from bundle')
    for item in bundle['artifacts']:
        path=Path(item['path'])
        if path.is_absolute() or '..' in path.parts:raise ValueError('unsafe evidence path')
        b=(root/path).read_bytes()
        if hashlib.sha256(b).hexdigest()!=item['sha256'] or len(b)!=item['bytes']:raise ValueError('stale evidence '+str(path))
    fingerprint=hashlib.sha256(json.dumps(bundle['artifacts'],sort_keys=True).encode()).hexdigest()
    if fingerprint!=bundle['evidence_fingerprint_sha256'] or fingerprint!=state['evidence_fingerprint_sha256']:raise ValueError('fingerprint mismatch')
    return True
if __name__=='__main__':
    try:validate();print('AI authority/hash/version validation PASS')
    except (ValueError,KeyError) as e:print(e);sys.exit(1)
