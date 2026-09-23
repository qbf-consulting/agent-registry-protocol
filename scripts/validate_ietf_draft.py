#!/usr/bin/env python3
"""Repository-local assurance checks for the ARPA Internet-Draft track."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DRAFT = ROOT / "ietf" / "draft-sankarshan-agent-registry-protocol.md"
HARDENING = ROOT / "ietf" / "fragments" / "adversarial-hardening.md"
PRECISION = ROOT / "ietf" / "fragments" / "protocol-precision.md"
AUTHORITY = ROOT / "ietf" / "fragments" / "authority-commitment.md"
README = ROOT / "ietf" / "README.md"
EXTRACTION = ROOT / "ietf" / "PROTOCOL_EXTRACTION.md"
PUBLISHED_CHECKLIST = ROOT / "ietf" / "SUBMISSION_CHECKLIST.md"
REVISION_CHECKLIST = ROOT / "ietf" / "REVISION_02_CHECKLIST.md"
BASELINE = ROOT / "ietf" / "REVISION_02_BASELINE.md"
DELTA = ROOT / "ietf" / "spec-delta-v02.yaml"
BUILD = ROOT / "scripts" / "build_ietf_draft.sh"
PRECISION_SPEC = ROOT / "spec" / "agent-registry-protocol-protocol-precision-pp01.md"
AUTHORITY_SPEC = ROOT / "spec" / "agent-registry-protocol-authority-commitment-pp02.md"
AUTHORITY_REQUIREMENTS = ROOT / "registries" / "authority-commitment-requirements-pp02.json"
PRECISION_REQUIREMENTS = ROOT / "registries" / "protocol-precision-requirements-pp01.json"
PRECISION_VECTORS = ROOT / "conformance" / "test-vectors" / "protocol-precision" / "protocol-precision-pp01.json"

errors = []
for path in (
    DRAFT,
    HARDENING,
    PRECISION,
    AUTHORITY,
    README,
    EXTRACTION,
    PUBLISHED_CHECKLIST,
    REVISION_CHECKLIST,
    BASELINE,
    DELTA,
    BUILD,
    PRECISION_SPEC,
    AUTHORITY_SPEC,
    AUTHORITY_REQUIREMENTS,
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

if AUTHORITY.exists():
    authority = AUTHORITY.read_text(encoding="utf-8")
    for needle in (
        "# Action-Specific Authority Evaluation",
        "canonical action digest",
        "Collective Principals",
        "MUST NOT be counted more than once",
        "# Relationship to Adjacent IETF Work",
        "{{WIMSE-ARCH}}",
        "{{WIMSE-CROSS-ORG}}",
        "{{RFC8693}}",
        "{{RFC9334}}",
        "{{RFC9943}}",
    ):
        if needle not in authority:
            errors.append(f"IETF -02 authority fragment missing required invariant/reference: {needle}")

if AUTHORITY_SPEC.exists():
    authority_spec = AUTHORITY_SPEC.read_text(encoding="utf-8")
    for needle in ("ARPA-CAND-PP-02", "Action-specific authority context", "Collective-principal authority"):
        if needle not in authority_spec:
            errors.append(f"PP-02 source missing required marker: {needle}")

if AUTHORITY_REQUIREMENTS.exists():
    req = AUTHORITY_REQUIREMENTS.read_text(encoding="utf-8")
    for needle in ("AC-PP02-001", "AC-PP02-010", "ARPA-CAND-PP-02"):
        if needle not in req:
            errors.append(f"PP-02 requirement registry missing marker: {needle}")

if PRECISION_SPEC.exists():
    precision_spec = PRECISION_SPEC.read_text(encoding="utf-8")
    if "ARPA-CAND-PP-01" not in precision_spec:
        errors.append("protocol precision source lost amendment identifier ARPA-CAND-PP-01")
    if "ARPA v0.9.0 Candidate Specification" not in precision_spec:
        errors.append("protocol precision source lost v0.9.0 normative baseline declaration")

if BUILD.exists():
    build = BUILD.read_text(encoding="utf-8")
    required_build = [
        'BASE="draft-sankarshan-agent-registry-protocol-02"',
        "protocol-precision.md",
        "authority-commitment.md",
        "RFC7595",
        "RFC8615",
        "agentreg:<registry-namespace>:<agent-local-id>",
        "requests permanent registration of the `agentreg` URI scheme",
        "URI suffix: `agent-registry`",
        "Status: Permanent",
        "WIMSE-CROSS-ORG",
        "RFC9943",
    ]
    for needle in required_build:
        if needle not in build:
            errors.append(f"-01 build path missing governed transformation: {needle}")

if DELTA.exists():
    delta = DELTA.read_text(encoding="utf-8")
    for proposition in ("ARPA-IETF-101", "ARPA-IETF-102", "ARPA-IETF-103"):
        if proposition not in delta:
            errors.append(f"IETF delta register missing accepted proposition {proposition}")
    if "published_baseline: draft-sankarshan-agent-registry-protocol-01" not in delta:
        errors.append("IETF delta register lost immutable -01 baseline declaration")
    if "target_revision: draft-sankarshan-agent-registry-protocol-02" not in delta:
        errors.append("IETF delta register lost -02 target declaration")

if REVISION_CHECKLIST.exists():
    checklist = REVISION_CHECKLIST.read_text(encoding="utf-8")
    for needle in (
        "Internet-Draft Revision `-02` Checklist",
        "Published `-01` identified as immutable baseline",
        "Action-specific authority context defined",
        "Collective-principal exercise semantics defined",
        "WIMSE architecture relationship explained",
        "OAuth 2.0 Token Exchange boundary explained",
        "make ietf-check",
        "generated RFCXML v3 reviewed",
        "Author Tools / submission checks completed",
    ):
        if needle not in checklist:
            errors.append(f"revision -02 checklist missing gate: {needle}")


if errors:
    print("IETF draft validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("IETF draft repository checks passed for governed -02 inputs and lifecycle state")
