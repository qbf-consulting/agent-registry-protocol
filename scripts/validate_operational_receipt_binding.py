#!/usr/bin/env python3
"""Model-only structural linkage of execution receipts, never authorization."""
import json
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker
ROOT=Path(__file__).resolve().parents[1]
schema=json.loads((ROOT/"schemas/execution-receipt.schema.json").read_text())
envelope=json.loads((ROOT/"schemas/common/envelope.schema.json").read_text())
schema["allOf"][0]=envelope  # Resolve repository-owned envelope locally, not over the network.\nvalidator=Draft202012Validator(schema,format_checker=FormatChecker())
def check(x):
    receipt=x["execution_receipt"]
    if list(validator.iter_errors(receipt)): return "invalid_receipt"
    decision=x["decision_receipt"]
    reliance=x["reliance_result"]
    if not decision.get("record_id") or not decision.get("decision"): return "unbound"
    if receipt["authority_decision_receipt"]!=decision["record_id"] or receipt["agent_id"]!=x["expected_agent_id"]: return "unbound"
    if reliance.get("authority_implication") is not False: return "unbound"
    if reliance.get("authority",{}).get("evidence_ref")!=x["expected_authority_evidence_ref"]: return "unbound"
    if decision["decision"] not in ("permit","deny","indeterminate"): return "unbound"
    if reliance["authority"]["decision"]!=decision["decision"]: return "inconsistent"
    if decision["decision"]!="permit" and receipt["result"]=="success": return "inconsistent"
    return "references_consistent"
def main():
    cases=json.loads((ROOT/"conformance/test-vectors/operational-receipt-binding/v0.1.0.json").read_text())["cases"]
    results=[{"id":x["id"],"expected":x["expected"],"actual":check(x["input"])} for x in cases]
    passed=bool(results) and all(x["actual"]==x["expected"] for x in results)
    print(json.dumps({"passed":passed,"cases":results,"limitations":["structural-only","no-cryptographic-evidence-verification","not-runtime-authorization"]},indent=2))
    raise SystemExit(0 if passed else 1)
if __name__=="__main__": main()
