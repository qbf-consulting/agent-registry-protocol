#!/usr/bin/env python3
from pathlib import Path
import json, subprocess, sys
ROOT=Path(__file__).resolve().parents[1]
r=subprocess.run([sys.executable,str(ROOT/'scripts/build_normative_requirements.py')],cwd=ROOT,capture_output=True,text=True)
if r.returncode:
    print(r.stdout+r.stderr); sys.exit(r.returncode)
cat=json.loads((ROOT/'registries/normative-requirements.json').read_text())
ids=[e['id'] for e in cat['entries']]
errors=[]
if len(ids)!=len(set(ids)): errors.append('duplicate normative requirement ids')
for e in cat['entries']:
    for k in ('id','section','requirement','verification_procedure','expected_evidence'):
        if not e.get(k): errors.append(f'{e.get("id","?")} missing {k}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
out=ROOT/'artifacts/conformance/normative-requirements-validation.json'; out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps({"status":"pass","catalogue":"registries/normative-requirements.json","requirements":len(ids),"unique_ids":len(set(ids)),"source":"spec/agent-registry-protocol-v0.10.0.md"},indent=2)+"\n")
print(f'validate_normative_requirements.py: PASS ({len(ids)} requirements)')
