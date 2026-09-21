#!/usr/bin/env python3
"""Repository-local assurance checks for the ARPA Internet-Draft track."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DRAFT = ROOT / "ietf" / "draft-sankarshan-agent-registry-protocol.md"
HARDENING = ROOT / "ietf" / "fragments" / "adversarial-hardening.md"
PRECISION = ROOT / "ietf" / "fragments" / "protocol-precision.md"
README = ROOT / "ietf" / "README.md"
EXTRACTION = ROOT / "ietf" / "PROTOCOL_EXTRACTION.md"
PUBLISHED_CHECKLIST = ROOT / "ietf" / "SUBMISSION_CHECKLIST.md"
REVISION_CHECKLIST = ROOT / "ietf" / "REVISION_01_CHECKLIST.md"
BASELINE = ROOT / "ietf" / "REVISION_01_BASELINE.md"
DELTA = ROOT / "ietf" / "spec-delta-v01.yaml"
BUILD = ROOT / "scripts" / "build_ietf_draft.sh"
PRECISION_SPEC = ROOT / "spec" / "agent-registry-protocol-protocol-precision-pp01.md"
PRECISION_REQUIREMENTS = ROOT / "registries" / "protocol-precision-requirements-pp01.json"
PRECISION_VECTORS = ROOT / "conformance" / "test-vectors" / "protocol-precision" / "protocol-precision-pp01.json"

errors = []
for path in (
    DRAFT,
    HARDENING,
    PRECISION,
    README,
    EXTRACTION,
    PUBLISHED_CHECKLIST,
    REVISION_CHECKLIST,
    BASELINE,
    DELTA,
    BUILD,
    PRECISION_SPEC,
    PRECISION_REQUIREMENTS,
    PRECISION_VECTORS,
):
    if not path.exists():
        errors.append(f"missing required IETF artifact: {path.relative_to(ROOT)}")

if DRAFT.exists():
    text = DRAFT.read_text(encoding="utf-8")
    required = [
        "docname: draft-sankarshan-agent-registry-protocol-00",
        "category: std",
        "ipr: trust200902",
        "# Security Considerations",
        "# Privacy Considerations",
        "# IANA Considerations",
        "RFC2119",
        "RFC8174",
        "RFC9110",
        "RFC9457",
    ]
    for needle in required:
        if needle not in text:
            errors.append(f"base draft source missing required marker: {needle}")

    if "CC BY 4.0" in text or "CC-BY-4.0" in text:
        errors.append("Internet-Draft body must not carry the project CC BY license notice")

    invariants = [
        "discovering an agent does not imply authorization",
        "capability does not imply permission",
        "technical federation does not imply governance recognition",
    ]
    lower = text.lower()
    for invariant in invariants:
        if invariant.lower() not in lower:
            errors.append(f"draft lost required non-implication invariant: {invariant}")

    for bad in ("layout: default", "nav_exclude:"):
        if bad in text:
            errors.append(f"IETF source contains project/Jekyll metadata: {bad}")

if HARDENING.exists():
    hardening = HARDENING.read_text(encoding="utf-8")
    required_hardening = [
        "# Adversarial Authority Processing",
        "semantic intersection",
        "half-open",
        "`not_applicable` is not an authority-failure result",
        "effective authoritative revocation immediately makes the revoked authority non-affirmative",
        "proof input transformation",
    ]
    for needle in required_hardening:
        if needle not in hardening:
            errors.append(f"IETF hardening fragment missing required invariant: {needle}")
    for bad in ("layout: default", "nav_exclude:", "CC BY 4.0", "CC-BY-4.0"):
        if bad in hardening:
            errors.append(f"IETF hardening fragment contains project-only metadata/license text: {bad}")

if PRECISION.exists():
    precision = PRECISION.read_text(encoding="utf-8")
    for needle in (
        "# Protocol Precision for Revision 01",
        "Historical resolution is a reconstruction operation",
        "Problem Details {{RFC9457}}",
        "Critical Extension Processing",
        "MUST NOT ignore the extension",
    ):
        if needle not in precision:
            errors.append(f"IETF precision fragment missing required invariant: {needle}")
    for bad in ("layout: default", "nav_exclude:", "CC BY 4.0", "CC-BY-4.0"):
        if bad in precision:
            errors.append(f"IETF precision fragment contains project-only metadata/license text: {bad}")

if PRECISION_SPEC.exists():
    precision_spec = PRECISION_SPEC.read_text(encoding="utf-8")
    if "ARPA-CAND-PP-01" not in precision_spec:
        errors.append("protocol precision source lost amendment identifier ARPA-CAND-PP-01")
    if "ARPA v0.9.0 Candidate Specification" not in precision_spec:
        errors.append("protocol precision source lost v0.9.0 normative baseline declaration")

if BUILD.exists():
    build = BUILD.read_text(encoding="utf-8")
    required_build = [
        'BASE="draft-sankarshan-agent-registry-protocol-01"',
        "protocol-precision.md",
        "RFC7595",
        "RFC8615",
        "agentreg:<registry-namespace>:<agent-local-id>",
        "requests permanent registration of the `agentreg` URI scheme",
        "URI suffix: `agent-registry`",
        "Status: Permanent",
    ]
    for needle in required_build:
        if needle not in build:
            errors.append(f"-01 build path missing governed transformation: {needle}")

if DELTA.exists():
    delta = DELTA.read_text(encoding="utf-8")
    for proposition in ("ARPA-IETF-001", "ARPA-IETF-002", "ARPA-IETF-003", "ARPA-IETF-004"):
        if proposition not in delta:
            errors.append(f"IETF delta register missing accepted proposition {proposition}")
    if "published_baseline: draft-sankarshan-agent-registry-protocol-00" not in delta:
        errors.append("IETF delta register lost immutable -00 baseline declaration")
    if "target_revision: draft-sankarshan-agent-registry-protocol-01" not in delta:
        errors.append("IETF delta register lost -01 target declaration")

if REVISION_CHECKLIST.exists():
    checklist = REVISION_CHECKLIST.read_text(encoding="utf-8")
    for needle in (
        "draft-sankarshan-agent-registry-protocol-01",
        "Published baseline",
        "Protocol diff review",
        "IETF submission hygiene",
        "idnits",
    ):
        if needle not in checklist:
            errors.append(f"revision -01 checklist missing gate: {needle}")

    published = "published and repository-closeout complete" in checklist
    if published:
        for needle in (
            "accepted and posted by the IETF on 2026-09-21",
            "No pre-publication submission gate remains open",
            "candidate work for `-02` or later",
        ):
            if needle not in checklist:
                errors.append(f"revision -01 published closeout missing marker: {needle}")
    else:
        for needle in (
            "repository-ready for merge",
            "not yet Datatracker-submission-ready",
        ):
            if needle not in checklist:
                errors.append(f"revision -01 pre-submission checklist missing gate: {needle}")

if errors:
    print("IETF draft validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("IETF draft repository checks passed for governed -01 inputs and lifecycle state")
