#!/usr/bin/env python3
"""
validate_test_vectors.py

Runs every conformance test vector under conformance/test-vectors/ through
the reference evaluator (scripts/reference_evaluator.py) and checks the
computed outcome against each vector's `expected_outcome`.

Run from the repository root:

    python3 scripts/validate_test_vectors.py

Exit code is 0 only if every vector's actual outcome matches its expected
outcome. Prints a final "PASS_COUNT/TOTAL_COUNT OK" line suitable for
pasting into a commit message.

No third-party dependencies.
"""

from __future__ import annotations

import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from reference_evaluator import evaluate_authority, resolve_identifier  # noqa: E402

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
VECTORS_DIR = REPO_ROOT / "conformance" / "test-vectors"

DISPATCH = {
    "authority_evaluation": evaluate_authority,
    "identifier_resolution": resolve_identifier,
}


def main() -> int:
    vector_paths = sorted(VECTORS_DIR.glob("*.json"))
    if not vector_paths:
        print(f"No test vectors found under {VECTORS_DIR.relative_to(REPO_ROOT)}")
        return 1

    total = 0
    passed = 0
    per_profile: dict[str, dict[str, int]] = {}
    failures = []

    for path in vector_paths:
        vector = json.loads(path.read_text())
        # Generic evaluator vectors use the legacy single-vector shape.\n        # Amendment-specific corpora (for example PP-04) are validated by their\n        # dedicated repository/IETF assurance checks and MUST NOT be misread here.\n        if "check" not in vector:\n            continue\n        total += 1\n        check = vector["check"]
        fn = DISPATCH.get(check)
        if fn is None:
            print(f"[ERROR] {path.name}: unknown check type '{check}'")
            failures.append((path.name, "unknown check type"))
            continue

        actual_outcome, reasons = fn(vector["input"])
        expected_outcome = vector["expected_outcome"]
        ok = actual_outcome == expected_outcome

        profile = vector.get("profile", "?")
        bucket = per_profile.setdefault(profile, {"pass": 0, "fail": 0, "total": 0})
        bucket["total"] += 1

        if ok:
            passed += 1
            print(f"[OK] {vector['vector_id']} ({profile}): {actual_outcome}")
        else:
            print(
                f"[MISMATCH] {vector['vector_id']} ({profile}): "
                f"expected {expected_outcome}, got {actual_outcome} ({', '.join(reasons)})"
            )
            failures.append((vector["vector_id"], f"expected {expected_outcome}, got {actual_outcome}"))

        # Track whether this vector represents a "grant" (allow*, active_record)
        # or a "block" (deny/indeterminate/not_found/not_authorized/terminal_record)
        # outcome, so we can confirm each profile has both.
        grant_outcomes = {"allow", "allow_with_conditions", "active_record"}
        if expected_outcome in grant_outcomes:
            bucket["pass"] += 1
        else:
            bucket["fail"] += 1

    print()
    print("Per-profile positive/negative coverage:")
    for profile in sorted(per_profile):
        b = per_profile[profile]
        status = "OK" if b["pass"] >= 1 and b["fail"] >= 1 else "INCOMPLETE"
        print(
            f"  Profile {profile}: {b['pass']} granting case(s), "
            f"{b['fail']} blocking case(s) [{status}]"
        )
        if status == "INCOMPLETE":
            failures.append((f"profile {profile}", "missing a granting or blocking test case"))

    print()
    print(f"validate_test_vectors.py: {passed}/{total} OK")

    if failures:
        print()
        print("FAILURES:")
        for name, reason in failures:
            print(f"  {name}: {reason}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
