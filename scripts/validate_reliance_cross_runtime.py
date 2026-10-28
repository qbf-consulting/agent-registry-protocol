#!/usr/bin/env python3
"""Prepare shared modeled dimensions and compare independent TypeScript composition results."""
import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/"scripts"))
from validate_operational_reliance import compose
from validate_operational_assessment import assess
from validate_operational_dependencies import evaluate

ART=ROOT/"artifacts/operational-reliance"
FIXTURES=ROOT/"conformance/test-vectors/operational-reliance/v0.1.0.json"

def prepare():
    tests=json.loads(FIXTURES.read_text())["cases"]
    out=[]
    for test in tests:
        try:
            composed=compose(test["input"])
            history=assess(test["input"]["operational_assessment"])
            deps=evaluate(test["input"]["dependency_assessment"])
        except (ValueError,KeyError,TypeError):
            # Invalid-input cases are owned by Python schema/validation, not the TS composition contract.
            continue
        values={"authority":composed["authority"]["decision"],
                "agent_status":composed["authoritative_state"]["agent_status"],
                "endpoint_status":composed["authoritative_state"]["endpoint_status"],
                "observation_outcome":history["assessment_outcome"],
                "freshness_evaluated":history["freshness"]["evaluated"],
                "dependency_readiness":deps["readiness"]}
        out.append({"id":test["id"],"dimensions":values,
                    "expected":{"outcome":composed["reliance"]["outcome"],
                      "reasons":composed["reliance"]["reasons"],"authority_implication":False}})
    if not out: raise ValueError("No valid modeled conformance vectors")
    ART.mkdir(parents=True,exist_ok=True)
    (ART/"cross-runtime-input.json").write_text(json.dumps({"cases":out},sort_keys=True,indent=2)+"\n")
    return len(out)

def compare():
    report=ART/"typescript-cross-runtime-report.json"
    if not report.exists(): raise ValueError("TypeScript report absent")
    data=json.loads(report.read_text())
    inputs=json.loads((ART/"cross-runtime-input.json").read_text())
    ids={item["id"] for item in inputs["cases"]}
    outcomes=data.get("results",[])
    ok=(data.get("passed") is True and len(outcomes)==len(ids)
        and {item["id"] for item in outcomes}==ids
        and all(item["passed"] is True for item in outcomes))
    summary={"passed":ok,"cases":len(outcomes),"scope":"independent TypeScript composition of Python-derived modeled dimensions",
             "limitations":["does-not-establish-independent-observation-or-federation-evaluation",
                            "does-not-establish-actual-execution-receipt-binding"]}
    (ART/"cross-runtime-comparison.json").write_text(json.dumps(summary,indent=2,sort_keys=True)+"\n")
    print(json.dumps(summary))
    return 0 if ok else 1

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--prepare",action="store_true")
    p.add_argument("--compare",action="store_true")
    args=p.parse_args()
    if args.prepare: print("Prepared "+str(prepare())+" shared vectors")
    if args.compare: raise SystemExit(compare())
    if not args.prepare and not args.compare: p.error("select --prepare or --compare")
