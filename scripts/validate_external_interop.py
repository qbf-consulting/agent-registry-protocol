#!/usr/bin/env python3
"""Validate ARPA's pinned external interoperability profile and evidence bundle.

This checks profile/report structure, vector pins, and artifact integrity. It
does not execute an implementation, authenticate an operator, or certify a
conformance claim.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
PROFILE_PATH = ROOT / "conformance" / "external" / "profile-v1.0.json"
SCHEMA_PATH = ROOT / "conformance" / "external" / "evidence-report.schema.json"
DEFAULT_REPORT = ROOT / "conformance" / "external" / "evidence-report-template.json"
PROFILE_ID = "arpa-external-implementation-interop"
PROFILE_VERSION = "1.0.0"


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"cannot read JSON {path}: {exc}") from exc


def selected_cases(profile: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """Verify suite digests and expected outcomes against pinned source vectors."""
    cases: dict[str, dict[str, Any]] = {}
    for suite in profile.get("suites", []):
        rel = suite.get("path", "")
        source_path = (ROOT / rel).resolve()
        if not source_path.is_relative_to(ROOT):
            raise ValueError(f"suite path escapes repository: {rel}")
        raw = source_path.read_bytes()
        actual_digest = hashlib.sha256(raw).hexdigest()
        if actual_digest != suite.get("sha256"):
            raise ValueError(f"{rel}: SHA-256 mismatch (profile={suite.get('sha256')}, actual={actual_digest})")
        source = json.loads(raw)
        vectors = {item.get("id"): item for item in source.get("vectors", [])}
        if len(vectors) != len(source.get("vectors", [])):
            raise ValueError(f"{rel}: duplicate or missing vector identifiers")
        for selection in suite.get("cases", []):
            case_id = selection.get("id")
            if not case_id or case_id in cases:
                raise ValueError(f"duplicate or missing selected case identifier: {case_id}")
            vector = vectors.get(case_id)
            if vector is None:
                raise ValueError(f"{rel}: selected vector not found: {case_id}")
            field = selection.get("expected_field")
            if field not in vector or vector[field] != selection.get("expected"):
                raise ValueError(f"{rel}:{case_id}: selected expected outcome differs from source vector")
            cases[case_id] = selection
    if not cases:
        raise ValueError("profile selects no cases")
    return cases


def validate_artifact(artifact: dict[str, Any], report_dir: Path) -> None:
    rel = artifact["path"]
    path = (report_dir / rel).resolve()
    if not path.is_relative_to(report_dir.resolve()):
        raise ValueError(f"artifact path escapes report directory: {rel}")
    if not path.is_file():
        raise ValueError(f"evidence artifact not found: {rel}")
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != artifact["sha256"]:
        raise ValueError(f"evidence artifact digest mismatch: {rel}")


def derive_assessment(report: dict[str, Any], required: dict[str, dict[str, Any]]) -> str:
    status = report["execution"]["status"]
    if status == "not_run":
        return "NOT_ESTABLISHED"
    results = report["results"]
    by_id = {result["case_id"]: result for result in results}
    if len(by_id) != len(results) or set(by_id) != set(required):
        return "INDETERMINATE"
    if status == "in_progress":
        return "INDETERMINATE"
    outcomes = []
    for case_id, result in by_id.items():
        expected = required[case_id]["expected"]
        if result["observed_outcome"] != expected or result["status"] != "pass":
            outcomes.append(result["status"])
            if result["observed_outcome"] != expected:
                outcomes.append("mismatch")
    if "fail" in outcomes or "mismatch" in outcomes:
        return "FAIL"
    if outcomes:
        return "INDETERMINATE"
    return "PASS"


def validate_report(report_path: Path) -> str:
    profile = load_json(PROFILE_PATH)
    if profile.get("profile_id") != PROFILE_ID or profile.get("profile_version") != PROFILE_VERSION:
        raise ValueError("unsupported external interoperability profile identity/version")
    required = selected_cases(profile)

    schema = load_json(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    report = load_json(report_path)
    errors = sorted(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(report), key=lambda e: list(e.path))
    if errors:
        details = "\n".join(f"{list(error.path)}: {error.message}" for error in errors)
        raise ValueError(f"evidence report does not match schema:\n{details}")
    if report["profile_id"] != PROFILE_ID or report["profile_version"] != PROFILE_VERSION:
        raise ValueError("evidence report does not identify this profile version")

    for artifact in report["artifacts"]:
        validate_artifact(artifact, report_path.parent)
    for result in report["results"]:
        if result["case_id"] not in required:
            raise ValueError(f"report contains an unselected case: {result['case_id']}")
        if result["status"] not in {"not_run"} and not result["evidence"]:
            raise ValueError(f"{result['case_id']}: result requires at least one evidence artifact")
        for artifact in result["evidence"]:
            validate_artifact(artifact, report_path.parent)

    return derive_assessment(report, required)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT, help="evidence report JSON (default: checked-in not-run template)")
    args = parser.parse_args()
    try:
        assessment = validate_report(args.report.resolve())
    except (KeyError, TypeError, ValueError, json.JSONDecodeError, OSError) as exc:
        print(f"external interoperability evidence invalid: {exc}")
        return 1
    print(f"external interoperability evidence structure: valid; assessment: {assessment}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
