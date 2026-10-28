#!/usr/bin/env python3
"""Model-level ARPA operational reliance composition, without acquiring authority.

Inputs for authoritative status and authority are *resolved scenario inputs*.
This module does not authenticate them, enforce decisions, or replace core ARPA.
"""
import json
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

from validate_operational_assessment import assess
from validate_operational_dependencies import evaluate as assess_dependencies

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "conformance/test-vectors/operational-reliance/v0.1.0.json"
SCHEMA = json.loads((ROOT / "schemas/operational-reliance-result.schema.json").read_text())

def compose(inputs):
    authority = inputs["authority"]
    current = inputs["current_state"]
    if authority.get("decision") not in ("permit", "deny", "indeterminate") or not authority.get("evidence_ref"):
        raise ValueError("resolved authority decision and source reference required")
    if current.get("agent_status") not in ("active", "revoked", "suspended", "unknown") or not current.get("evidence_ref"):
        raise ValueError("current authoritative status and provenance required")
    if current.get("endpoint_status") not in ("available", "offline", "unknown"):
        raise ValueError("unsupported endpoint status")
    history = assess(inputs["operational_assessment"])
    dependencies = assess_dependencies(inputs["dependency_assessment"])
    if history["authority_implication"] or dependencies["authority_implication"]:
        raise ValueError("derived evidence may not amplify authority")
    reasons = []
    # Authority and lifecycle state always take priority, never overwritten by reachability.
    if authority["decision"] == "deny" or current["agent_status"] in ("revoked", "suspended"):
        outcome = "deny"
        reasons.append("authority_or_lifecycle_denial")
    else:
        if authority["decision"] != "permit" or current["agent_status"] != "active":
            reasons.append("authority_not_positively_established")
        if current["endpoint_status"] != "available":
            reasons.append("current_endpoint_state_not_available")
        if history["assessment_outcome"] != "observations_present" or not history["freshness"]["evaluated"]:
            reasons.append("operational_evidence_insufficient_or_unchecked")
        if dependencies["readiness"] != "prerequisites_observed":
            reasons.append("critical_dependencies_not_established")
        outcome = "not_established" if reasons else "prerequisites_observed"
    result = {
        "profile_version": "0.1.0",
        "authority": {"decision": authority["decision"], "evidence_ref": authority["evidence_ref"]},
        "authoritative_state": {"agent_status": current["agent_status"], "endpoint_status": current["endpoint_status"], "evidence_ref": current["evidence_ref"]},
        "operational_evidence": {"outcome": history["assessment_outcome"], "observation_ids": history["source_observation_ids"], "freshness_evaluated": history["freshness"]["evaluated"]},
        "dependencies": {"readiness": dependencies["readiness"], "reasons": dependencies["reasons"], "snapshot_digest": dependencies["snapshot_digest"]},
        "reliance": {"outcome": outcome, "reasons": sorted(reasons)},
        "authority_implication": False
    }
    errs = list(Draft202012Validator(SCHEMA,format_checker=FormatChecker()).iter_errors(result))
    if errs:
        raise ValueError("invalid reliance representation: " + errs[0].message)
    return result

def validate_fixtures():
    tests = json.loads(FIXTURES.read_text(encoding="utf-8"))["cases"]
    results = []
    seen = set()
    for item in tests:
        if item["id"] in seen:
            raise ValueError("duplicate integration case")
        seen.add(item["id"])
        try:
            output = compose(item["input"])
            actual = output["reliance"]["outcome"]
            valid = actual == item["expected"]
            for path, expected in item.get("expected_fields",{}).items():
                val=output
                for part in path.split("."):
                    val=val[part]
                valid = valid and val == expected
        except (ValueError,KeyError,TypeError) as exc:
            actual = "error"
            valid = item["expected"] == "error"
        results.append({"id":item["id"],"expected":item["expected"],"actual":actual,"passed":valid})
    return {"passed":bool(results) and all(x["passed"] for x in results), "cases":results,
            "limitations":["modeled-resolved-authority","no-live-federation-or-evidence-verification","not-a-runtime-enforcement-engine"]}

if __name__ == "__main__":
    report=validate_fixtures()
    print(json.dumps(report,indent=2))
    raise SystemExit(0 if report["passed"] else 1)
