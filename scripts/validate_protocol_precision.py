#!/usr/bin/env python3
"""Validate ARPA v0.9.2 protocol-precision amendment and cross-artifact alignment."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
VECTORS_REL = "conformance/test-vectors/protocol-precision/protocol-precision-v0.9.2.json"


def load_json(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


amendment = ROOT / "spec/agent-registry-protocol-v0.9.2-protocol-precision.md"
requirements_path = ROOT / "registries/protocol-precision-requirements-v0.9.2.json"
vectors_path = ROOT / VECTORS_REL
openapi_path = ROOT / "openapi/arpa-openapi.yaml"
historical_schema_path = ROOT / "schemas/historical-resolution.schema.json"
error_registry_path = ROOT / "registries/error-codes.json"
extension_registry_path = ROOT / "registries/extension-namespaces.json"
delta_path = ROOT / "ietf/spec-delta-v01.yaml"

for path in (
    amendment,
    requirements_path,
    vectors_path,
    openapi_path,
    historical_schema_path,
    error_registry_path,
    extension_registry_path,
    delta_path,
):
    if not path.exists():
        errors.append(f"missing protocol-precision artifact: {path.relative_to(ROOT)}")

if amendment.exists():
    text = amendment.read_text(encoding="utf-8")
    required_markers = [
        "agentreg:<registry-namespace>:<agent-local-id>",
        "Historical resolution is a reconstruction operation",
        "RFC 9457 Problem Details",
        "unknown-critical-extension",
        "Cross-artifact consistency",
    ]
    for marker in required_markers:
        if marker not in text:
            errors.append(f"precision amendment missing marker: {marker}")

vectors = load_json(VECTORS_REL) if vectors_path.exists() else {}
if vectors:
    if vectors.get("arpa_version") != "0.9.2":
        errors.append("protocol-precision vectors must declare arpa_version 0.9.2")
    entries = vectors.get("vectors", [])
    ids = [entry.get("id") for entry in entries]
    if len(entries) < 14:
        errors.append("protocol-precision suite must contain at least 14 vectors")
    if len(ids) != len(set(ids)):
        errors.append("duplicate protocol-precision vector id")
    expected_ids = {f"PREC-{n:03d}" for n in range(1, 15)}
    if set(ids) != expected_ids:
        errors.append("protocol-precision vector ids must be PREC-001 through PREC-014")

requirements = load_json("registries/protocol-precision-requirements-v0.9.2.json") if requirements_path.exists() else {}
if requirements:
    if requirements.get("arpa_version") != "0.9.2":
        errors.append("protocol-precision requirements must declare arpa_version 0.9.2")
    entries = requirements.get("entries", [])
    ids = [entry.get("id") for entry in entries]
    if len(entries) < 14:
        errors.append("protocol-precision requirement catalogue must contain at least 14 entries")
    if len(ids) != len(set(ids)):
        errors.append("duplicate protocol-precision requirement id")
    known_vectors = {entry.get("id") for entry in vectors.get("vectors", [])}
    for entry in entries:
        for field in ("id", "section", "requirement", "verification", "expected_evidence"):
            if not entry.get(field):
                errors.append(f"{entry.get('id', '<unknown>')} missing {field}")
        for verification in entry.get("verification", []):
            if verification != "inspection" and verification not in known_vectors:
                errors.append(f"{entry.get('id', '<unknown>')} references unknown vector {verification}")

if openapi_path.exists():
    openapi = openapi_path.read_text(encoding="utf-8")
    if "pattern: '^agentreg:'" not in openapi:
        errors.append("OpenAPI AgentId no longer constrains identifiers to agentreg")
    if "application/problem+json" not in openapi or "code:" not in openapi:
        errors.append("OpenAPI does not expose the ARPA Problem Details code contract")
    if "historical-resolution" not in openapi:
        errors.append("OpenAPI historical-resolution operation is missing")

if historical_schema_path.exists():
    schema = load_json("schemas/historical-resolution.schema.json")
    required = set(schema.get("required", []))
    for field in (
        "requested_time",
        "evaluation_time",
        "reconstruction_status",
        "selected_records",
        "later_material_events",
        "evidence",
    ):
        if field not in required:
            errors.append(f"historical-resolution schema missing required field {field}")

if error_registry_path.exists():
    codes = {entry.get("id") for entry in load_json("registries/error-codes.json").get("entries", [])}
    required_codes = {
        "ARPA-EXT-CRITICAL-UNKNOWN",
        "ARPA-AUTHORITY-INDETERMINATE",
        "ARPA-HISTORICAL-EVIDENCE-UNAVAILABLE",
        "ARPA-HISTORICAL-EVIDENCE-CONFLICT",
        "ARPA-HISTORICAL-INTEGRITY-FAILURE",
    }
    missing = required_codes - codes
    if missing:
        errors.append(f"error registry missing required protocol-precision codes: {sorted(missing)}")

if extension_registry_path.exists():
    extension_entries = load_json("registries/extension-namespaces.json").get("entries", [])
    if not extension_entries:
        errors.append("extension namespace registry is empty")
    for entry in extension_entries:
        if not entry.get("id") or not entry.get("status"):
            errors.append("extension namespace entry missing id or status")

if delta_path.exists():
    delta = delta_path.read_text(encoding="utf-8")
    for proposition in ("ARPA-IETF-001", "ARPA-IETF-002", "ARPA-IETF-003", "ARPA-IETF-004"):
        if proposition not in delta:
            errors.append(f"IETF delta register missing {proposition}")

if errors:
    print("Protocol precision validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

out = ROOT / "artifacts/conformance/protocol-precision-validation.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(
    json.dumps(
        {
            "status": "pass",
            "arpa_version": "0.9.2",
            "requirements": len(requirements.get("entries", [])),
            "vectors": len(vectors.get("vectors", [])),
            "checks": [
                "agentreg-identifier-alignment",
                "historical-resolution-contract",
                "rfc9457-problem-contract",
                "critical-extension-fail-safe",
                "ietf-delta-traceability",
            ],
        },
        indent=2,
    )
    + "\n",
    encoding="utf-8",
)
print(
    "validate_protocol_precision.py: PASS "
    f"({len(requirements.get('entries', []))} requirements; "
    f"{len(vectors.get('vectors', []))} vectors)"
)
