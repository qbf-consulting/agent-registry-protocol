#!/usr/bin/env python3
"""Compare repository-owned Python, TypeScript and bounded Rust outcomes.

Python and TypeScript remain the broad deterministic comparison. The Rust
experiment is required only for Profile A identifier-resolution vectors and is
explicitly marked out of scope for authority-evaluation and historical checks.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from reference_evaluator import evaluate_authority, resolve_identifier  # noqa: E402

TS_REPORT = ROOT / "artifacts" / "typescript" / "conformance-report.json"
RUST_REPORT = ROOT / "artifacts" / "rust" / "conformance-report.json"
TS_HISTORICAL = ROOT / "artifacts" / "typescript" / "historical-resolution-report.json"
PY_HISTORICAL = ROOT / "artifacts" / "historical-resolution" / "evidence-bundle.json"
OUT = ROOT / "artifacts" / "typescript" / "cross-runtime-report.json"


def python_outcome(vector: dict) -> str:
    if vector["check"] == "identifier_resolution":
        return resolve_identifier(vector["input"])[0]
    if vector["check"] == "authority_evaluation":
        return evaluate_authority(vector["input"])[0]
    raise ValueError(f"unsupported check: {vector['check']}")


def main() -> int:
    required = (TS_REPORT, RUST_REPORT, TS_HISTORICAL, PY_HISTORICAL)
    missing = [path for path in required if not path.exists()]
    if missing:
        raise SystemExit(
            "Required assurance report missing: "
            + ", ".join(str(path.relative_to(ROOT)) for path in missing)
        )

    ts = json.loads(TS_REPORT.read_text())
    ts_results = {item["vector_id"]: item for item in ts["results"]}
    rust = json.loads(RUST_REPORT.read_text())
    rust_results = {item["vector_id"]: item for item in rust["results"]}
    deterministic = []

    for path in sorted((ROOT / "conformance" / "test-vectors").glob("TV-*.json")):
        vector = json.loads(path.read_text())
        py = python_outcome(vector)
        ts_item = ts_results.get(vector["vector_id"])
        ts_outcome = ts_item["actual"] if ts_item else None
        expected = vector["expected_outcome"]

        rust_required = vector["check"] == "identifier_resolution"
        rust_item = rust_results.get(vector["vector_id"]) if rust_required else None
        rust_outcome = rust_item["actual"] if rust_item else None
        rust_status = (
            "executed"
            if rust_required and rust_item
            else "missing_required_evidence"
            if rust_required
            else "not_in_experiment_scope"
        )

        equivalent = (
            py == ts_outcome == rust_outcome == expected
            if rust_required
            else py == ts_outcome == expected
        )
        deterministic.append(
            {
                "vector_id": vector["vector_id"],
                "check": vector["check"],
                "expected": expected,
                "python": py,
                "typescript": ts_outcome,
                "rust": rust_outcome,
                "rust_status": rust_status,
                "equivalent": equivalent,
            }
        )

    py_hist = {
        item["id"]: item
        for item in json.loads(PY_HISTORICAL.read_text())["results"]
    }
    ts_hist = {
        item["id"]: item
        for item in json.loads(TS_HISTORICAL.read_text())["results"]
    }
    historical = []
    for vector_id in sorted(set(py_hist) | set(ts_hist)):
        py_item = py_hist.get(vector_id)
        ts_item = ts_hist.get(vector_id)
        equivalent = bool(
            py_item
            and ts_item
            and py_item["passed"]
            and ts_item["passed"]
            and py_item["reconstruction_status"]
            == ts_item["reconstruction_status"]
            and py_item["historical_effect"] == ts_item["historical_effect"]
        )
        historical.append(
            {
                "vector_id": vector_id,
                "python_reconstruction_status": (
                    py_item.get("reconstruction_status") if py_item else None
                ),
                "typescript_reconstruction_status": (
                    ts_item.get("reconstruction_status") if ts_item else None
                ),
                "rust_status": "not_in_experiment_scope",
                "python_historical_effect": (
                    py_item.get("historical_effect") if py_item else None
                ),
                "typescript_historical_effect": (
                    ts_item.get("historical_effect") if ts_item else None
                ),
                "equivalent": equivalent,
            }
        )

    deterministic_passed = sum(1 for item in deterministic if item["equivalent"])
    historical_passed = sum(1 for item in historical if item["equivalent"])
    rust_identifier = [
        item for item in deterministic if item["check"] == "identifier_resolution"
    ]
    rust_identifier_passed = sum(
        1
        for item in rust_identifier
        if item["rust_status"] == "executed"
        and item["rust"] == item["expected"]
        and item["equivalent"]
    )
    total = len(deterministic) + len(historical)
    equivalent = deterministic_passed + historical_passed

    report = {
        "report_type": "arpa-cross-runtime-conformance",
        "arpa_baseline": "0.9.4",
        "candidate_specification": "v0.10.0",
        "implementations": [
            "ARPA Python reference/evidence path",
            "ARPA TypeScript v0.3.0",
            "ARPA bounded Rust identifier-resolution experiment v0.1.0",
        ],
        "independence_boundary": (
            "Implementations share governed vectors but not behavioral implementation "
            "code. All three remain repository-owned and do not establish external "
            "organizational independence."
        ),
        "surfaces": {
            "deterministic_conformance": {
                "total": len(deterministic),
                "equivalent": deterministic_passed,
                "comparisons": deterministic,
            },
            "rust_identifier_resolution": {
                "total": len(rust_identifier),
                "equivalent": rust_identifier_passed,
                "scope": "Profile A identifier_resolution only",
            },
            "historical_resolution": {
                "total": len(historical),
                "equivalent": historical_passed,
                "comparisons": historical,
            },
        },
        "total": total,
        "equivalent": equivalent,
        "passed": (
            equivalent == total
            and rust_identifier_passed == len(rust_identifier)
            and bool(rust_identifier)
        ),
        "limitations": [
            "Repository-owned runtime diversity is L1 cross-runtime evidence, not external organisational independence.",
            "The Rust experiment is intentionally limited to Profile A identifier resolution; unsupported checks are recorded as not_in_experiment_scope rather than PASS.",
            "Historical comparison proves equivalent interpretation of the bounded repository vector corpus; it is not network retrieval interoperability.",
            "Network-level Python-TypeScript interoperability is reported separately in artifacts/typescript/network-interoperability-report.json.",
        ],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    print(
        f"Cross-runtime equivalence: {equivalent}/{total} checks "
        f"({deterministic_passed}/{len(deterministic)} deterministic; "
        f"{historical_passed}/{len(historical)} historical; "
        f"{rust_identifier_passed}/{len(rust_identifier)} Rust identifier-resolution)"
    )
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
