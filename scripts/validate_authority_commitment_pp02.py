#!/usr/bin/env python3
"""Validate ARPA-CAND-PP-02 authority-at-commitment amendment traceability."""
from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "spec" / "agent-registry-protocol-authority-commitment-pp02.md"
REQ = ROOT / "registries" / "authority-commitment-requirements-pp02.json"
VECTORS = ROOT / "conformance" / "test-vectors" / "authority-at-commitment"

errors: list[str] = []

if not SPEC.is_file():
    errors.append("missing PP-02 Candidate amendment")
if not REQ.is_file():
    errors.append("missing PP-02 requirement registry")
if not VECTORS.is_dir():
    errors.append("missing authority-at-commitment vector directory")

if SPEC.is_file():
    text = SPEC.read_text(encoding="utf-8")
    for marker in (
        "ARPA-CAND-PP-02",
        "Action-specific authority context",
        "Current authority and constraint preservation",
        "Approval binding",
        "Collective-principal authority",
        "Separation from authentication and execution",
        "IETF extraction boundary",
    ):
        if marker not in text:
            errors.append(f"PP-02 specification missing marker: {marker}")

if REQ.is_file():
    data = json.loads(REQ.read_text(encoding="utf-8"))
    if data.get("amendment") != "ARPA-CAND-PP-02":
        errors.append("PP-02 requirement registry has wrong amendment identifier")
    requirements = data.get("requirements") or []
    ids = {item.get("id") for item in requirements}
    expected = {f"AC-PP02-{i:03d}" for i in range(1, 11)}
    if ids != expected:
        errors.append(f"PP-02 requirement IDs differ from expected set: {sorted(ids)}")
    levels = {item.get("level") for item in requirements}
    if not levels.issubset({"MUST", "MUST_NOT", "SHOULD"}):
        errors.append(f"unexpected PP-02 requirement level(s): {sorted(levels)}")

if VECTORS.is_dir():
    vectors = []
    for path in sorted(VECTORS.glob("*.json")):
        vectors.append(json.loads(path.read_text(encoding="utf-8")))
    ids = {v.get("vector_id") for v in vectors}
    for required in ("AAC-01", "AAC-04", "AAC-05", "AAC-06", "AAC-07", "AAC-08", "AAC-09", "AAC-10"):
        if required not in ids:
            errors.append(f"authority-at-commitment evidence missing {required}")
    outcomes = {v.get("expected_outcome") for v in vectors}
    if not {"allow", "deny", "indeterminate"}.issubset(outcomes):
        errors.append("authority-at-commitment evidence must cover allow, deny and indeterminate outcomes")

if errors:
    print("PP-02 authority-at-commitment validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("PP-02 authority-at-commitment traceability checks passed")
