#!/usr/bin/env python3
"""Bounded optional dependency evaluation; never determines delegated authority."""
import json
import hashlib
import argparse
from datetime import datetime
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT=Path(__file__).resolve().parents[1]
SCHEMA=json.loads((ROOT/"schemas/operational-dependency.schema.json").read_text())
FIXTURES=ROOT/"conformance/test-vectors/operational-dependency/v0.1.0.json"
VALIDATOR=Draft202012Validator(SCHEMA,format_checker=FormatChecker())

def parse_time(text):
    try:
        value=datetime.fromisoformat(text.replace("Z","+00:00"))
        if value.tzinfo is None or value.utcoffset() is None:
            raise ValueError("timestamp requires timezone")
        return value
    except (ValueError,TypeError,AttributeError) as exc:
        raise ValueError("invalid offset-aware timestamp") from exc

def cycles(edges):
    graph={}
    for a,b in edges: graph.setdefault(a,set()).add(b)
    visiting,visited=set(),set()
    def visit(node):
        if node in visiting: return True
        if node in visited: return False
        visiting.add(node)
        result=any(visit(child) for child in sorted(graph.get(node,())))
        visiting.remove(node)
        visited.add(node)
        return result
    return any(visit(node) for node in sorted(graph))

def evaluate(case):
    deps=case["dependencies"]
    ids=set()
    now=parse_time(case["evaluated_at"]) if "evaluated_at" in case else None
    edges=[]
    for dep in deps:
        if list(VALIDATOR.iter_errors(dep)):
            raise ValueError("invalid dependency declaration")
        if dep["dependency_id"] in ids:
            raise ValueError("duplicate dependency ID")
        ids.add(dep["dependency_id"])
        edges.append((dep["dependent_agent"],dep["required_service"]))
        begin=parse_time(dep["applicable_from"]) if "applicable_from" in dep else None
        end=parse_time(dep["applicable_until"]) if "applicable_until" in dep else None
        if begin and end and begin>=end:
            raise ValueError("invalid applicability interval")
        if (begin or end) and now is None:
            raise ValueError("evaluation time required for temporal dependency")
    if any(dep.get("cycle_policy")=="prohibit" for dep in deps) and cycles(edges):
        raise ValueError("cycle prohibited by declared dependency profile")
    snapshot_digest = "sha256:" + hashlib.sha256(json.dumps(sorted(deps,key=lambda d:d["dependency_id"]),sort_keys=True,separators=(",",":")).encode("utf-8")).hexdigest()
    expected_snapshot = case.get("expected_snapshot_digest")
    if expected_snapshot is not None and expected_snapshot != snapshot_digest:
        return {"readiness":"indeterminate","authority_implication":False,"reasons":["dependency_snapshot_mismatch"],"snapshot_digest":snapshot_digest}
    observations=case.get("observed_states",{})
    issues={"unavailable":[],"indeterminate":[]}
    for dep in deps:
        if dep["criticality"]!="critical": continue
        did=dep["dependency_id"]
        begin=dep.get("applicable_from")
        end=dep.get("applicable_until")
        if now and ((begin and now<parse_time(begin)) or (end and now>=parse_time(end))):
            issues["indeterminate"].append(did)
            continue
        registry=dep.get("registry_context",{})
        if registry and not registry["recognized"]:
            issues["indeterminate"].append(did)
            continue
        state=observations.get(dep["required_service"])
        # Unknown, stale and contradictory states never produce an affirmative result.
        if isinstance(state,list):
            if len(set(state))!=1: state="conflicting"
            elif state: state=state[0]
        if state=="unavailable":issues["unavailable"].append(did)
        elif state!="available":issues["indeterminate"].append(did)
    readiness="unavailable" if issues["unavailable"] else ("indeterminate" if issues["indeterminate"] or not deps else "prerequisites_observed")
    return {"readiness":readiness,"authority_implication":False,"reasons":sorted(issues["unavailable"]+issues["indeterminate"]),"snapshot_digest":snapshot_digest}

def validate():
    cases=json.loads(FIXTURES.read_text())["cases"]
    results=[]
    for case in cases:
        try:
            actual=evaluate(case["input"])
            outcome=actual["readiness"]
            passed=outcome==case["expected"] and all(actual.get(k)==v for k,v in case.get("expected_fields",{}).items())
        except ValueError:
            outcome="error"
            passed=case["expected"]=="error"
        results.append({"id":case["id"],"expected":case["expected"],"actual":outcome,"passed":passed})
    return {"passed":bool(results) and all(x["passed"] for x in results),"cases":results,"limitations":["modeled-fixtures","declared-states-not-verified","not-authority-or-lifecycle-evaluation"]}
if __name__=="__main__":
    cli=argparse.ArgumentParser()
    cli.add_argument("--output",type=Path,default=ROOT/"artifacts/operational-dependency/validation-report.json")
    args=cli.parse_args()
    report=validate()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
    print(json.dumps(report,indent=2))
    raise SystemExit(0 if report["passed"] else 1)
