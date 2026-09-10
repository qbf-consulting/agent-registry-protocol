#!/usr/bin/env python3
"""Repository-local assurance checks for the ARPA Internet-Draft track."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DRAFT = ROOT / "ietf" / "draft-sankarshan-agent-registry-protocol.md"
HARDENING = ROOT / "ietf" / "fragments" / "adversarial-hardening.md"
README = ROOT / "ietf" / "README.md"
EXTRACTION = ROOT / "ietf" / "PROTOCOL_EXTRACTION.md"
CHECKLIST = ROOT / "ietf" / "SUBMISSION_CHECKLIST.md"

errors = []
for path in (DRAFT, HARDENING, README, EXTRACTION, CHECKLIST):
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
            errors.append(f"draft missing required marker: {needle}")

    if "CC BY 4.0" in text or "CC-BY-4.0" in text:
        errors.append("Internet-Draft body must not carry the project CC BY license notice")

    # Core non-implication semantics must remain visible in the protocol extraction.
    invariants = [
        "discovering an agent does not imply authorization",
        "capability does not imply permission",
        "technical federation does not imply governance recognition",
    ]
    lower = text.lower()
    for invariant in invariants:
        if invariant.lower() not in lower:
            errors.append(f"draft lost required non-implication invariant: {invariant}")

    # Guard against accidental reintroduction of Jekyll publication metadata.
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

if errors:
    print("IETF draft validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("IETF draft repository checks passed")
