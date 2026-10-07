import json
from pathlib import Path

import pytest

from scripts.validate_external_interop import (
    PROFILE_ID,
    PROFILE_VERSION,
    derive_assessment,
    selected_cases,
    validate_report,
)

ROOT = Path(__file__).resolve().parents[1]
PROFILE = json.loads((ROOT / "conformance/external/profile-v1.0.json").read_text())


def test_checked_in_template_is_valid_but_not_evidence():
    report = ROOT / "conformance/external/evidence-report-template.json"
    assert validate_report(report) == "NOT_ESTABLISHED"


def test_profile_selects_exactly_16_pinned_cases():
    assert len(selected_cases(PROFILE)) == 16


def test_changed_vector_outcome_is_rejected():
    profile = json.loads(json.dumps(PROFILE))
    profile["suites"][0]["cases"][0]["expected"] = "accept"
    with pytest.raises(ValueError, match="differs from source vector"):
        selected_cases(profile)


def test_incomplete_complete_run_is_indeterminate():
    required = selected_cases(PROFILE)
    case_id = next(iter(required))
    report = {
        "execution": {"status": "complete"},
        "results": [{"case_id": case_id, "status": "pass", "observed_outcome": required[case_id]["expected"], "evidence": [{}]}],
    }
    assert derive_assessment(report, required) == "INDETERMINATE"


def test_complete_mismatch_cannot_be_reported_as_pass():
    required = selected_cases(PROFILE)
    results = [
        {"case_id": case_id, "status": "pass", "observed_outcome": selection["expected"], "evidence": [{}]}
        for case_id, selection in required.items()
    ]
    results[0]["observed_outcome"] = "wrong"
    assert derive_assessment({"execution": {"status": "complete"}, "results": results}, required) == "FAIL"


def test_complete_run_with_all_selected_cases_and_matching_outcomes_passes():
    required = selected_cases(PROFILE)
    results = [
        {"case_id": case_id, "status": "pass", "observed_outcome": selection["expected"], "evidence": [{}]}
        for case_id, selection in required.items()
    ]
    assert derive_assessment({"execution": {"status": "complete"}, "results": results}, required) == "PASS"


def test_artifact_digest_is_checked(tmp_path):
    import hashlib

    artifact = tmp_path / "trace.json"
    artifact.write_text('{"outcome":"allow"}', encoding="utf-8")
    digest = hashlib.sha256(artifact.read_bytes()).hexdigest()
    from scripts.validate_external_interop import validate_artifact

    descriptor = {"path": "trace.json", "sha256": "0" * 64, "media_type": "application/json"}
    with pytest.raises(ValueError, match="digest mismatch"):
        validate_artifact(descriptor, tmp_path)
    descriptor["sha256"] = digest
    validate_artifact(descriptor, tmp_path)
