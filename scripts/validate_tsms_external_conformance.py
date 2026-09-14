#!/usr/bin/env python3
"""Validate ARPA's adopter-side TSMM/TIS conformance experiment.

This validator intentionally does not fetch remote schemas. ARPA pins the
profile and portable contract identity in its declaration and validates its
own evidence and fail-safe behavior locally. Cross-repository contract shape
is validated in TIS; semantic profile integrity is validated in TSMM.
"""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DECLARATION_PATH = ROOT / "conformance" / "tsms" / "external-conformance-declaration.json"
PRESSURE_PATH = ROOT / "conformance" / "tsms" / "pressure-tests.json"

PROFILE_ID = "tsmm-external-conformance-core-2026.1"
PROFILE_VERSION = "1.0.0"
REQUIRED_IDS = {
    "TSMM-CONF-AUTHORITY",
    "TSMM-CONF-DELEGATION",
    "TSMM-CONF-SCOPE",
    "TSMM-CONF-CURRENT-STATE",
    "TSMM-CONF-EVIDENCE",
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def decision(requirements: list[dict], *, profile_id: str = PROFILE_ID, profile_version: str = PROFILE_VERSION) -> str:
    if profile_id != PROFILE_ID or profile_version != PROFILE_VERSION:
        return "FAIL"

    by_id = {item.get("id"): item for item in requirements}
    if set(by_id) != REQUIRED_IDS:
        return "FAIL"

    for item in requirements:
        if item.get("support") in {"unsupported", "unknown"}:
            return "FAIL"
        evidence = item.get("evidence")
        if not isinstance(evidence, list) or not evidence:
            return "INDETERMINATE"
    return "PASS"


def validate_evidence_paths(declaration: dict) -> list[str]:
    errors: list[str] = []
    for requirement in declaration.get("requirements", []):
        for evidence in requirement.get("evidence", []):
            path = ROOT / evidence
            if not path.exists():
                errors.append(f"{requirement.get('id')}: evidence path not found: {evidence}")
    return errors


def execute_case(case: dict, declaration: dict) -> str:
    candidate = deepcopy(declaration)
    requirements = candidate["requirements"]
    condition = case["condition"]

    if condition == "all-required-supported-with-evidence":
        return decision(requirements)
    if condition == "missing-authority":
        requirements[:] = [r for r in requirements if r["id"] != "TSMM-CONF-AUTHORITY"]
    elif condition == "missing-delegation":
        requirements[:] = [r for r in requirements if r["id"] != "TSMM-CONF-DELEGATION"]
    elif condition == "out-of-scope-effect":
        next(r for r in requirements if r["id"] == "TSMM-CONF-SCOPE")["support"] = "unsupported"
    elif condition == "revoked-or-non-current-state":
        next(r for r in requirements if r["id"] == "TSMM-CONF-CURRENT-STATE")["support"] = "unsupported"
    elif condition == "missing-required-evidence":
        next(r for r in requirements if r["id"] == "TSMM-CONF-EVIDENCE")["evidence"] = []
    elif condition == "unknown-semantic-requirement":
        requirements.append({"id": "TSMM-CONF-UNKNOWN", "support": "supported", "evidence": ["README.md"]})
    elif condition == "unsupported-profile-version":
        return decision(requirements, profile_version="99.0.0")
    else:
        raise ValueError(f"unknown pressure-test condition: {condition}")

    return decision(requirements)


def main() -> None:
    declaration = load(DECLARATION_PATH)
    pressure = load(PRESSURE_PATH)

    if declaration.get("profile_id") != PROFILE_ID or declaration.get("profile_version") != PROFILE_VERSION:
        raise SystemExit("ARPA declaration does not pin the supported TSMM profile")
    if declaration.get("implementation", {}).get("name") != "agent-registry-protocol":
        raise SystemExit("ARPA declaration implementation identity is invalid")

    requirement_ids = [item.get("id") for item in declaration.get("requirements", [])]
    if len(requirement_ids) != len(set(requirement_ids)):
        raise SystemExit("ARPA declaration contains duplicate requirement identifiers")
    if set(requirement_ids) != REQUIRED_IDS:
        raise SystemExit(f"ARPA declaration must contain exactly the required profile ids: {sorted(REQUIRED_IDS)}")

    evidence_errors = validate_evidence_paths(declaration)
    if evidence_errors:
        raise SystemExit("\n".join(evidence_errors))

    if decision(declaration["requirements"]) != "PASS":
        raise SystemExit("complete ARPA declaration did not evaluate to PASS")

    cases = pressure.get("cases", [])
    if not cases:
        raise SystemExit("pressure-test corpus is empty")

    seen = set()
    for case in cases:
        case_id = case.get("id")
        if not case_id or case_id in seen:
            raise SystemExit(f"duplicate or missing pressure-test id: {case_id}")
        seen.add(case_id)
        actual = execute_case(case, declaration)
        if actual != case.get("expected"):
            raise SystemExit(f"{case_id}: expected {case.get('expected')}, got {actual}")

    print(f"ARPA TSMS external conformance passed: declaration + {len(cases)} pressure tests")


if __name__ == "__main__":
    main()
