#!/usr/bin/env python3
import json
from pathlib import Path
p=Path("conformance/test-vectors/adversarial/authority-laundering-v0.10.0.json")
d=json.loads(p.read_text())
assert d["arpa_version"]=="0.10.0"
assert d["suite"]=="authority-laundering-adversarial"
assert any("SIMULATION_01_RUNBOOK.md" in x for x in d["research_provenance"])
ids={v["id"] for v in d["vectors"]}
assert ids=={f"AUTH-LAUNDER-00{i}" for i in range(1,6)}
for v in d["vectors"][:4]:
    assert "allow" in v["prohibited_decisions"]
    assert "allow_with_conditions" in v["prohibited_decisions"]
e=d["vectors"][4]
assert e["scenario"]=="evidence-change-resolves-predicate-without-authority-change"
assert "authority_grant_inferred" in e["prohibited_decisions"]
assert "authority_state_unchanged" in e["required_evidence"]
print("Authority laundering adversarial vectors: PASS")
