from scripts.validate_tsms_external_conformance import (
    PROFILE_ID,
    PROFILE_VERSION,
    REQUIRED_IDS,
    decision,
)


def complete_requirements():
    return [
        {"id": requirement_id, "support": "supported", "evidence": ["README.md"]}
        for requirement_id in sorted(REQUIRED_IDS)
    ]


def test_complete_required_profile_passes():
    assert decision(complete_requirements()) == "PASS"


def test_missing_required_semantic_fails():
    requirements = complete_requirements()[1:]
    assert decision(requirements) == "FAIL"


def test_unsupported_required_semantic_fails():
    requirements = complete_requirements()
    requirements[0]["support"] = "unsupported"
    assert decision(requirements) == "FAIL"


def test_missing_required_evidence_is_indeterminate():
    requirements = complete_requirements()
    requirements[0]["evidence"] = []
    assert decision(requirements) == "INDETERMINATE"


def test_unknown_semantic_identifier_fails():
    requirements = complete_requirements()
    requirements.append({"id": "TSMM-CONF-UNKNOWN", "support": "supported", "evidence": ["README.md"]})
    assert decision(requirements) == "FAIL"


def test_future_profile_version_fails_closed():
    assert decision(complete_requirements(), profile_id=PROFILE_ID, profile_version="99.0.0") == "FAIL"


def test_unknown_profile_id_fails_closed():
    assert decision(complete_requirements(), profile_id="unknown-profile", profile_version=PROFILE_VERSION) == "FAIL"
