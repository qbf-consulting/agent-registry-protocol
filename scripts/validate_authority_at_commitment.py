#!/usr/bin/env python3
"""Validate action-specific authority-at-commitment conformance vectors.

This evaluator is intentionally bounded to the informative projection in
`docs/authority-at-commitment.md`. It does not modify the Candidate
Specification's reference evaluator.
"""
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
VECTORS = ROOT / "conformance" / "test-vectors" / "authority-at-commitment"


def parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def evaluate(data: dict) -> str:
    state = data.get("authority_state")
    if state is None or state == "unavailable":
        return "indeterminate"
    if state != "active":
        return "deny"

    envelope = data.get("authority_envelope")
    request = data.get("request")
    if not envelope or not request:
        return "indeterminate"

    now = parse_time(request["time"])
    if now < parse_time(envelope["effective_from"]):
        return "deny"
    if envelope.get("effective_until") and now > parse_time(envelope["effective_until"]):
        return "deny"
    if request.get("action") not in envelope.get("action_classes", []):
        return "deny"
    resources = envelope.get("resource_scope") or []
    if resources and request.get("resource") not in resources:
        return "deny"

    limit = (envelope.get("limits") or {}).get("amount_max")
    if limit is not None and request.get("amount") is not None and request["amount"] > limit:
        return "deny"

    required = envelope.get("required_approvals") or []
    if required:
        approval = data.get("approval")
        if approval is None:
            return "deny"
        if approval.get("action_digest") != request.get("action_digest"):
            return "deny"
        if approval.get("valid_until") and parse_time(approval["valid_until"]) < now:
            return "deny"

    collective = data.get("collective_authority")
    if collective is not None:
        if not isinstance(collective, dict):
            return "indeterminate"

        membership_evidence = collective.get("membership_evidence")
        rule_evidence = collective.get("rule_evidence")
        if membership_evidence in {None, "missing", "unknown", "unavailable"}:
            return "indeterminate"
        if rule_evidence in {None, "missing", "unknown", "unavailable"}:
            return "indeterminate"
        if membership_evidence != "current" or rule_evidence != "current":
            return "deny"

        threshold = collective.get("threshold_required")
        members = collective.get("current_members")
        approvals = collective.get("approvals")
        if not isinstance(threshold, int) or threshold < 1:
            return "indeterminate"
        if not isinstance(members, list) or not members:
            return "indeterminate"
        if threshold > len(set(members)):
            return "deny"
        if approvals is None or not isinstance(approvals, list):
            return "indeterminate"

        current_members = set(members)
        qualifying_members = set()
        for approval in approvals:
            if not isinstance(approval, dict):
                return "deny"
            member = approval.get("member")
            if member not in current_members:
                return "deny"
            if approval.get("action_digest") != request.get("action_digest"):
                return "deny"
            if approval.get("valid_until") and parse_time(approval["valid_until"]) < now:
                return "deny"
            if approval.get("valid") is not True:
                return "deny"
            qualifying_members.add(member)

        if len(qualifying_members) < threshold:
            return "deny"

    return "allow"


def main() -> int:
    paths = sorted(VECTORS.glob("*.json"))
    if not paths:
        print("No authority-at-commitment vectors found")
        return 1

    failures: list[str] = []
    granting = blocking = 0
    for path in paths:
        vector = json.loads(path.read_text())
        actual = evaluate(vector["input"])
        expected = vector["expected_outcome"]
        if expected == "allow":
            granting += 1
        else:
            blocking += 1
        if actual != expected:
            failures.append(f"{vector['vector_id']}: expected {expected}, got {actual}")
            print(f"[FAIL] {failures[-1]}")
        else:
            print(f"[OK] {vector['vector_id']}: {actual}")

    if granting < 1 or blocking < 1:
        failures.append("profile requires at least one granting and one blocking vector")

    if failures:
        print("\n".join(failures))
        return 1

    print(f"validate_authority_at_commitment.py: {len(paths)}/{len(paths)} OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
