#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, re, sys
ROOT=Path(__file__).resolve().parents[1]
SPEC=ROOT/'spec/agent-registry-protocol-v0.10.0.md'
OUT=ROOT/'registries/normative-requirements.json'
EVIDENCE='artifacts/conformance/normative-requirements-validation.json'
TERMS=re.compile(r'\b(MUST(?: NOT)?|REQUIRED|SHALL(?: NOT)?|SHOULD(?: NOT)?|RECOMMENDED|MAY|OPTIONAL)\b')
heading='front-matter'
entries=[]
for raw in SPEC.read_text().splitlines():
    line=raw.strip()
    m=re.match(r'^#{1,6}\s+(.+)$',line)
    if m:
        heading=m.group(1); continue
    if not line or line.startswith('```') or line.startswith('|'): continue
    if not TERMS.search(line): continue
    norm=' '.join(line.split())
    digest=hashlib.sha256(norm.encode()).hexdigest()[:10].upper()
    secm=re.match(r'^(\d+(?:\.\d+)*(?:[A-Z])?)\b',heading)
    sec=secm.group(1) if secm else 'CTRL'
    rid='ARPA-NORM-'+sec.replace('.','-')+'-'+digest
    entries.append({"id":rid,"section":heading,"requirement":norm,"verification_procedure":"scripts/validate_normative_requirements.py","expected_evidence":EVIDENCE})
# de-dupe exact IDs while preserving order
seen=set(); entries=[e for e in entries if not (e['id'] in seen or seen.add(e['id']))]
data={"registry":"normative-requirements","version":"0.10.0","source":"spec/agent-registry-protocol-v0.10.0.md","id_policy":"content-derived; changes only when the normative clause changes","entries":entries}
if '--write' in sys.argv:
    OUT.write_text(json.dumps(data,indent=2)+"\n")
else:
    existing=json.loads(OUT.read_text())
    if existing!=data:
        print('normative requirement catalogue is stale; run scripts/build_normative_requirements.py --write')
        sys.exit(1)
print(f'build_normative_requirements.py: {len(entries)} requirements')
