#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from datetime import datetime
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []

def load(rel: str):
    return json.loads((ROOT / rel).read_text())

def section_codes(text: str, heading: str, next_heading: str) -> set[str]:
    start = text.find(heading)
    end = text.find(next_heading, start + len(heading))
    if start < 0 or end < 0:
        errors.append(f"cannot locate Candidate section {heading}")
        return set()
    return set(re.findall(r"`([A-Za-z0-9_.-]+)`", text[start:end]))

spec = (ROOT / "spec/agent-registry-protocol-v0.9.0.md").read_text()

# Candidate prose -> controlled registry coherence.
candidate_events = section_codes(spec, "## 24.2 Event Types", "## 24.3 Event Envelope")
event_registry = load("registries/event-types.json")
event_ids = {e["id"] for e in event_registry["entries"]}
event_base = {e["id"] for e in event_registry["entries"] if e.get("class") == "candidate_base"}
event_schema = load("schemas/event.schema.json")
event_enum = set(event_schema["properties"]["event_type"]["enum"])
if event_base != candidate_events:
    errors.append(f"base event registry drift: Candidate-only={sorted(candidate_events-event_base)} registry-only={sorted(event_base-candidate_events)}")
if event_enum != event_ids:
    errors.append(f"event schema/registry drift: schema-only={sorted(event_enum-event_ids)} registry-only={sorted(event_ids-event_enum)}")

candidate_errors = section_codes(spec, "## 34.2 Base Error Codes", "## 34.3 HTTP Status Code Mapping")
error_registry = load("registries/error-codes.json")
error_base = {e["id"] for e in error_registry["entries"] if e.get("class") == "candidate_base"}
if error_base != candidate_errors:
    errors.append(f"base error registry drift: Candidate-only={sorted(candidate_errors-error_base)} registry-only={sorted(error_base-candidate_errors)}")

candidate_relationships = section_codes(spec, "## 13.4 Relationship Record", "## 13.5 Key Binding Record")
relationship_ids = {e["id"] for e in load("registries/relationship-types.json")["entries"]}
relationship_schema = load("schemas/relationship.schema.json")
relationship_enum = set(relationship_schema["allOf"][1]["properties"]["relationship_type"]["enum"])
if relationship_ids != candidate_relationships or relationship_enum != relationship_ids:
    errors.append("relationship prose/registry/schema vocabulary drift")

lifecycle_ids = {e["id"] for e in load("registries/lifecycle-statuses.json")["entries"]}
status_registration = set(load("schemas/status.schema.json")["properties"]["registration"]["enum"])
if lifecycle_ids != status_registration:
    errors.append("lifecycle registry/status schema registration drift")

# Deprecated namespace placeholders must never remain active.
extensions = load("registries/extension-namespaces.json")["entries"]
for e in extensions:
    if e.get("status") == "active" and "arpa.example" in e["id"]:
        errors.append("placeholder arpa.example namespace remains active")
    if e.get("status") == "active" and not (
        e["id"].startswith("https://qbfconsulting.digital/ns/arpa/")
        or e.get("class") == "external"
    ):
        errors.append(f"active namespace lacks controlled/collision-resistant classification: {e['id']}")

# Problem Details code/type contract.
problem_schema = load("schemas/problem-details.schema.json")
problem_validator = Draft202012Validator(problem_schema)
for entry in error_registry["entries"]:
    code = entry["id"]
    problem = {
        "type": error_registry["problem_type_base"] + code,
        "title": code,
        "status": 400,
        "code": code,
    }
    if list(problem_validator.iter_errors(problem)):
        errors.append(f"registered error cannot be represented as ARPA Problem Details: {code}")

# Authority result / not_applicable semantics.
result_schema = load("schemas/authority-evaluation-result.schema.json")
result_validator = Draft202012Validator(result_schema)
vectors = load("conformance/test-vectors/wire-contract/wire-contract-pp03.json")["vectors"]
by_id = {v["id"]: v for v in vectors}
for required in [f"WC-{n:03d}" for n in range(1,17)]:
    if required not in by_id:
        errors.append(f"missing PP-03 vector {required}")

na = by_id.get("WC-003", {})
sample = {
    "decision": na.get("expected_outcome"),
    "reason_codes": na.get("input", {}).get("reason_codes", []),
    "evaluation_time": "2026-09-23T00:00:00Z",
    "policy": {"id": "policy:test", "version": "1", "applicable": na.get("input", {}).get("applicable")},
}
if list(result_validator.iter_errors(sample)):
    errors.append("legitimate not_applicable result does not validate")
for vid in ("WC-004", "WC-005"):
    if "not_applicable" not in set(by_id.get(vid, {}).get("prohibited_outcomes", [])):
        errors.append(f"{vid} must explicitly prohibit not_applicable")

# Half-open time semantics.
def dt(value: str):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))

for vid in ("WC-006", "WC-007", "WC-008"):
    v = by_id.get(vid)
    if not v:
        continue
    inp = v["input"]
    actual = dt(inp["effective_from"]) <= dt(inp["evaluation_time"]) < dt(inp["effective_until"])
    if actual != v["expected_in_interval"]:
        errors.append(f"{vid} violates half-open interval semantics")

clock = by_id.get("WC-009", {})
if clock.get("expected_outcome") not in ("deny", "indeterminate"):
    errors.append("clock-ambiguous material state must be non-affirmative")

# Collective snapshot/churn semantics.
def collective(v: dict) -> str:
    inp = v["input"]
    sid = inp.get("snapshot_id")
    if not sid or not inp.get("current_members"):
        return "indeterminate"
    approvals = inp.get("approvals")
    if not isinstance(approvals, list):
        return "indeterminate"
    qualifying = set()
    members = set(inp["current_members"])
    for approval in approvals:
        if approval.get("snapshot_id") != sid:
            return "deny"
        if approval.get("member") not in members:
            return "deny"
        qualifying.add(approval["member"])
    return "allow" if len(qualifying) >= inp["threshold"] else "deny"

for vid in ("WC-010", "WC-011", "WC-012"):
    v = by_id.get(vid)
    if v and collective(v) != v["expected_outcome"]:
        errors.append(f"{vid} collective snapshot result mismatch")

# Parent authority link is canonical and represented in the schema.
authority_schema = load("schemas/authority-envelope.schema.json")
props = authority_schema["allOf"][1]["properties"]
if "derives_from" not in props:
    errors.append("authority envelope lacks derives_from")
parent = by_id.get("WC-013", {}).get("input", {})
if not parent.get("derives_from"):
    errors.append("delegated parent-link vector lacks derives_from")

# OpenAPI binds the exact schemas and preserves Candidate media type.
openapi = (ROOT / "openapi/arpa-openapi.yaml").read_text()
for needle in (
    "application/agent-registry+json",
    "../schemas/authority-evaluation-result.schema.json",
    "../schemas/problem-details.schema.json",
):
    if needle not in openapi:
        errors.append(f"OpenAPI missing PP-03 binding: {needle}")
if "application/arpa+json" in openapi:
    errors.append("OpenAPI introduced prohibited application/arpa+json spelling")

# Machine requirements trace to known vectors/evidence.
req = load("registries/wire-contract-requirements-pp03.json")
known = set(by_id)
for entry in req.get("entries", []):
    for field in ("id", "title", "section", "requirement", "verification", "expected_evidence"):
        if not entry.get(field):
            errors.append(f"{entry.get('id','<unknown>')} missing {field}")
    for vector_id in entry.get("verification", []):
        if vector_id not in known:
            errors.append(f"{entry['id']} references unknown vector {vector_id}")

if errors:
    print("\n".join(errors))
    sys.exit(1)

out = ROOT / "artifacts/conformance/wire-contract-pp03-validation.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps({
    "status": "pass",
    "amendment": "ARPA-CAND-PP-03",
    "candidate_base_events": len(candidate_events),
    "registered_event_values": len(event_ids),
    "candidate_base_errors": len(candidate_errors),
    "relationship_types": len(relationship_ids),
    "lifecycle_registration_states": len(lifecycle_ids),
    "vectors": len(vectors),
    "checks": [
        "candidate-registry-schema-vocabulary-coherence",
        "not-applicable-wire-semantics",
        "half-open-time-boundaries",
        "clock-ambiguity-fail-safe",
        "collective-snapshot-binding",
        "parent-authority-linkage",
        "rfc9457-problem-details",
        "media-type-preservation",
        "extension-namespace-authority",
        "pp03-requirement-traceability",
    ],
}, indent=2) + "\n")
print(f"validate_wire_contract_pp03.py: PASS ({len(vectors)} vectors)")
