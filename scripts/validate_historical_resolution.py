from pathlib import Path
import json, sys
from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas/historical-resolution.schema.json"
VECTOR_DIR = ROOT / "conformance/test-vectors/historical"
ARTIFACT_DIR = ROOT / "artifacts/historical-resolution"

schema = json.loads(SCHEMA_PATH.read_text())
status_schema = json.loads((ROOT / "schemas/status.schema.json").read_text())
registry = Registry().with_resource(status_schema["$id"], Resource.from_contents(status_schema))
validator = Draft202012Validator(schema, registry=registry, format_checker=FormatChecker())
manifest = json.loads((VECTOR_DIR / "manifest.json").read_text())
errors = []
results = []

for vector in manifest["vectors"]:
    path = VECTOR_DIR / vector["path"]
    if not path.exists():
        errors.append(f"missing historical vector: {vector['path']}")
        continue
    data = json.loads(path.read_text())
    validation_errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
    if validation_errors:
        errors.extend(f"{vector['id']}: schema: {e.message}" for e in validation_errors)
        continue
    if data["reconstruction_status"] != vector["expected_reconstruction_status"]:
        errors.append(f"{vector['id']}: reconstruction status mismatch")
    if data["historical_effect"] != vector["expected_historical_effect"]:
        errors.append(f"{vector['id']}: historical effect mismatch")
    if data["requested_time"] < data["evaluation_time"] and data["state_at_requested_time"] == data["current_state"] and vector["id"] == "HV-12-current-state-not-substituted":
        errors.append("HV-12: current state substituted for historical state")
    if data["evidence"]["integrity_status"] == "failed" and data["reconstruction_status"] not in ("indeterminate", "reconstructed_partial", "authoritative_partial"):
        errors.append(f"{vector['id']}: integrity failure yielded unqualified historical result")
    if data["retention"]["status"] == "outside_retention" and data["reconstruction_status"] != "indeterminate":
        errors.append(f"{vector['id']}: retention boundary must be indeterminate")
    results.append({"id": vector["id"], "passed": True, "reconstruction_status": data["reconstruction_status"], "historical_effect": data["historical_effect"]})

if errors:
    print("\n".join(errors))
    sys.exit(1)

ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
evidence = {"profile": manifest["profile"], "version": manifest["version"], "passed": True, "vector_count": len(results), "results": results}
(ARTIFACT_DIR / "evidence-bundle.json").write_text(json.dumps(evidence, indent=2) + "\n")
print(f"validate_historical_resolution.py: {len(results)}/{len(manifest['vectors'])} historical vectors passed")

# Explicit optional bitemporal profile: exercise selection and fail-safe cases,
# not merely schema shape. This is independent of the TypeScript implementation.
from datetime import datetime

def timestamp(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))

def select_bitemporal(records, ctx):
    def fail(reason):
        return ("indeterminate", [], reason)
    try:
        e, cutoff, now = (timestamp(ctx[k]) for k in ("effective_at", "evidence_as_of", "evaluation_time"))
        cover = timestamp(ctx["history_complete_through"]) if ctx.get("history_complete_through") else None
        for r in records:
            timestamp(r["effective_from"])
            if r.get("effective_until") is not None:
                timestamp(r["effective_until"])
            if r.get("recorded_at") is not None:
                timestamp(r["recorded_at"])
    except (ValueError, KeyError, TypeError):
        return fail("invalid_temporal_input")
    if e > now or cutoff > now:
        return fail("cutoff_or_effective_time_after_evaluation")
    if cover is None or cover < cutoff:
        return fail("incomplete_authoritative_record_history")
    if any(not r.get("recorded_at") for r in records):
        return fail("missing_authoritative_recording_time")
    if any(not r.get("logical_key") or not r.get("record_id") for r in records):
        return fail("missing_record_identity")
    if len({r["record_id"] for r in records}) != len(records):
        return fail("duplicate_record_identity")
    known = [r for r in records if timestamp(r["recorded_at"]) <= cutoff]
    identities = {r["record_id"] for r in known}
    effective = [r for r in known if timestamp(r["effective_from"]) <= e and
                 (r.get("effective_until") is None or e < timestamp(r["effective_until"]))]
    if any(any(i not in identities for i in r.get("supersedes", [])) for r in effective):
        return fail("unknown_supersession_target")
    if any(r["record_id"] in r.get("supersedes", []) for r in effective):
        return fail("self_supersession")
    replaced = {i for r in effective for i in r.get("supersedes", [])}
    selected = [r for r in effective if r["record_id"] not in replaced]
    if len({r["logical_key"] for r in selected}) != len(selected):
        return fail("contradictory_effective_claims_without_supersession")
    return ("determinate", sorted(r["record_id"] for r in selected), "complete_authoritative_history_at_cutoff")

bitemporal = json.loads((ROOT / "conformance/test-vectors/bitemporal/fixtures.json").read_text())
for vector in bitemporal["vectors"]:
    actual = select_bitemporal(vector["records"], vector["context"])
    expected = vector["expected"]
    if actual != (expected["outcome"], expected["selected_record_ids"], expected["reason_code"]):
        print(f"bitemporal {vector['id']}: expected {expected}, got {actual}")
        sys.exit(1)
print(f"validate_historical_resolution.py: {len(bitemporal['vectors'])} bitemporal evaluation vectors passed")
