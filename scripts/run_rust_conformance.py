#!/usr/bin/env python3
"""Execute the bounded Rust identifier-resolution experiment.

The harness parses the repository-owned shared vectors, invokes independently
implemented Rust behavior, and emits machine-readable evidence. It intentionally
does not translate Python evaluator logic into Rust.
"""
from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "rust" / "Cargo.toml"
VECTORS = ROOT / "conformance" / "test-vectors"
OUT = ROOT / "artifacts" / "rust" / "conformance-report.json"


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )


def bool_arg(value: object, default: bool) -> str:
    resolved = default if value is None else bool(value)
    return "true" if resolved else "false"


def main() -> int:
    if shutil.which("cargo") is None:
        raise SystemExit("cargo is required for the Rust interoperability experiment")

    run("cargo", "test", "--quiet", "--manifest-path", str(MANIFEST))
    run("cargo", "build", "--quiet", "--manifest-path", str(MANIFEST))
    binary = ROOT / "rust" / "target" / "debug" / "arpa-rust-identifier-resolution"

    results = []
    for path in sorted(VECTORS.glob("TV-A-*.json")):
        vector = json.loads(path.read_text())
        if vector.get("check") != "identifier_resolution":
            continue
        payload = vector["input"]
        completed = run(
            str(binary),
            "--known", bool_arg(payload.get("known"), False),
            "--terminal", bool_arg(payload.get("terminal"), False),
            "--authorized-caller", bool_arg(payload.get("authorized_caller"), True),
        )
        decision = json.loads(completed.stdout)
        expected = vector["expected_outcome"]
        results.append(
            {
                "vector_id": vector["vector_id"],
                "fixture": str(path.relative_to(ROOT)),
                "expected": expected,
                "actual": decision["outcome"],
                "reason_codes": decision["reason_codes"],
                "passed": decision["outcome"] == expected,
            }
        )

    report = {
        "report_type": "arpa-rust-identifier-resolution-experiment",
        "normative_baseline": "ARPA Candidate v0.10.0",
        "implementation": "repository-owned Rust experiment",
        "implementation_version": "0.1.0",
        "operation": "identifier_resolution",
        "profile": "A",
        "source": "rust/",
        "shared_fixture_glob": "conformance/test-vectors/TV-A-*.json",
        "results": results,
        "total": len(results),
        "passed": sum(1 for item in results if item["passed"]),
        "all_passed": bool(results) and all(item["passed"] for item in results),
        "unsupported_checks": ["authority_evaluation", "historical_resolution", "registry_mutation"],
        "independence_claim": False,
        "limitations": [
            "Repository-owned Rust code is L1 cross-runtime evidence, not external organizational independence.",
            "The experiment covers only Profile A identifier resolution.",
            "The Rust artifact has no HTTP, persistence, federation, authority-evaluation, or historical-resolution surface.",
            "Successful resolution does not imply recognition, trust, capability, or authorization.",
        ],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    print(f"Rust identifier resolution: {report['passed']}/{report['total']} vectors passed")
    return 0 if report["all_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
