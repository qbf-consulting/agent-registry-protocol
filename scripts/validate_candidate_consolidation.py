#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, re, sys

ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/'conformance/manifests/candidate-consolidation-v0.10.0.json'
SPEC=ROOT/'spec/agent-registry-protocol-v0.10.0.md'
OUT=ROOT/'artifacts/conformance/candidate-consolidation-v0.10.0-validation.json'
TERMS=re.compile(r'\b(MUST(?: NOT)?|REQUIRED|SHALL(?: NOT)?|SHOULD(?: NOT)?|RECOMMENDED|MAY|OPTIONAL)\b')

def git_blob_sha(path):
    data=path.read_bytes()
    return hashlib.sha1(b'blob '+str(len(data)).encode()+bytes([0])+data).hexdigest()

def extract_section(text,prefix):
    lines=text.splitlines()
    start=next((i for i,l in enumerate(lines) if l.startswith('## '+prefix)),None)
    if start is None:
        raise ValueError(f'missing source section {prefix}')
    end=len(lines)
    for i in range(start+1,len(lines)):
        if lines[i].startswith('## '):
            end=i; break
    return '\n'.join(lines[start+1:end]).strip()

def adapt(text):
    return (text.replace('This amendment','This specification')
                .replace('this amendment','this specification')
                .replace('the amendment','the specification')
                .replace('ARPA v0.9.0 Candidate','ARPA v0.10.0 Candidate')
                .replace('v0.9.0 Candidate Specification','v0.10.0 Candidate Specification'))

def norm(s):
    return ' '.join(s.split())

m=json.loads(MANIFEST.read_text())
spec=SPEC.read_text()
errors=[]
if '**Version:** 0.10.0' not in spec: errors.append('v0.10.0 version marker missing')
if '**Intended Status:** Candidate Specification' not in spec: errors.append('Candidate status marker missing')
if 'sole authoritative prose specification for ARPA v0.10.0' not in spec: errors.append('v0.10.0 authority control missing')
if 'IETF extraction boundary' in spec: errors.append('IETF extraction process text leaked into consolidated protocol body')

for sid,meta in m['sources'].items():
    p=ROOT/meta['path']
    if git_blob_sha(p)!=meta['git_blob_sha']:
        errors.append(f'historical source changed: {meta["path"]}')

normalized_spec=norm(spec)
checked=0
for item in m['mappings']:
    meta=m['sources'][item['source']]
    body=adapt(extract_section((ROOT/meta['path']).read_text(),item['section']))
    if f'consolidated-source: {item["marker"]}' not in spec:
        errors.append(f'missing provenance marker: {item["marker"]}')
    for raw in body.splitlines():
        line=raw.strip()
        if not line or line.startswith('|') or line.startswith('```') or not TERMS.search(line):
            continue
        checked+=1
        if norm(line) not in normalized_spec:
            errors.append(f'normative carry-over missing: {item["marker"]}: {norm(line)[:180]}')

for item in m['published_ietf_02_control_files']:
    p=ROOT/item['path']
    if git_blob_sha(p)!=item['git_blob_sha']:
        errors.append(f'published -02 control file changed during consolidation: {item["path"]}')

if errors:
    print('\n'.join(errors))
    sys.exit(1)
OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text(json.dumps({'status':'pass','candidate_version':'0.10.0','mapped_amendment_sections':len(m['mappings']),'normative_carry_over_assertions':checked,'historical_sources_frozen':len(m['sources']),'ietf_02_control_files_frozen':len(m['published_ietf_02_control_files'])},indent=2)+'\n')
print(f'validate_candidate_consolidation.py: PASS ({len(m["mappings"])} sections; {checked} normative carry-over assertions)')
