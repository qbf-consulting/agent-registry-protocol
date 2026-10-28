#!/usr/bin/env python3
"""Optional, non-authoritative operational dependency readiness assessment."""
import json
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parents[1]
SCHEMA=json.loads((ROOT/"schemas/operational-dependency.schema.json").read_text())
FIXTURES=ROOT/"conformance/test-vectors/operational-dependency/v0.1.0.json"

def evaluate(case):
    validator=Draft202012Validator(SCHEMA)
    deps=case["dependencies"]
    ids=set()
    for dep in deps:
        if list(validator.iter_errors(dep)):
            raise ValueError("invalid dependency declaration")
        if dep["dependency_id"] in ids:
            raise ValueError("duplicate dependency ID")
        ids.add(dep["dependency_id"])
    observations=case["observed_states"]
    for dep in deps:
        if dep["criticality"]!="critical":
            continue
        state=observations.get(dep["required_service"])
        if state=="unavailable":
            return {"readiness":"unavailable","authority_implication":False,"reasons":[dep["dependency_id"]]}
        if state not in ("available",):
            return {"readiness":"indeterminate","authority_implication":False,"reasons":[dep["dependency_id"]]}
    return {"readiness":"prerequisites_observed","authority_implication":False,"reasons":[]}

def validate():
    cases=json.loads(FIXTURES.read_text())["cases"]
    results=[]
    for case in cases:
        try:
            actual=evaluate(case["input"])
            outcome=actual["readiness"]
        except ValueError:
            outcome="error"
        results.append({"id":case["id"],"expected":case["expected"],"actual":outcome,"passed":outcome==case["expected"]})
    return {"passed":bool(results) and all(x["passed"] for x in results),"cases":results,"limitations":["modeled-fixtures","declared-states-not-verified","not-authority-or-lifecycle-evaluation"]}
if __name__=="__main__":
    print(json.dumps(validate(),indent=2))
    raise SystemExit(0 if validate()["passed"] else 1)
