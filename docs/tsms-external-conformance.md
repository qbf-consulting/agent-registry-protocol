---
layout: default
title: "TSMS External Conformance Experiment"
---

# TSMS external conformance experiment

ARPA is the first implementation outside the TSMS repositories used to pressure-test the candidate TSMM external semantic conformance profile and the TIS portable evidence contracts.

This is an **adopter-side conformance experiment**, not a certification claim and not a normative incorporation of TSMS into ARPA.

## Authority boundary

ARPA remains authoritative for ARPA protocol semantics, implementation behavior, releases, and conformance evidence. TSMM remains authoritative for the semantic profile requirements it publishes. TIS remains authoritative for the portable JSON contracts used to serialize declarations and results.

ARPA does not acquire authority to redefine a TSMM requirement. TSMM/TIS do not acquire authority over ARPA merely because ARPA declares support for a profile.

## Declaration

The machine-readable adopter declaration is:

- [`conformance/tsms/external-conformance-declaration.json`](../conformance/tsms/external-conformance-declaration.json)

It binds ARPA v0.9.5 to the candidate `tsmm-external-conformance-core-2026.1` profile and provides repository-local evidence for:

- authority;
- delegation;
- scope;
- current/revoked state;
- evidence availability.

Evidence references point to ARPA's existing normative specification, hardening amendment, candidate evidence, and conformance corpus. No TSMS-specific normative semantics are added to ARPA to manufacture a pass.

## Pressure tests

[`conformance/tsms/pressure-tests.json`](../conformance/tsms/pressure-tests.json) deliberately falsifies the safe path. The repository validator proves that:

- absent authority fails;
- absent delegation fails;
- out-of-scope effects fail;
- revoked or non-current state fails;
- missing required evidence is `INDETERMINATE`;
- an unknown semantic requirement fails;
- an unsupported profile version fails.

Run:

```bash
python3 scripts/validate_tsms_external_conformance.py
```

The validator is also included in `make validate` and therefore in the release gate.

## Why ARPA validates locally

ARPA does not fetch moving remote schemas during deterministic release validation. TIS validates the portable schema contracts in the TIS repository; TSMM validates profile integrity in TSMM; ARPA pins the supported profile identity/version and validates its own evidence and fail-safe decision behavior locally.

This preserves independently reproducible repository gates while still making cross-repository authority and compatibility explicit.

## Non-claims

A `PASS` from this experiment means only that ARPA's declared evidence satisfies the bounded candidate profile as exercised by the published tests. It does not establish external certification, production assurance, legal compliance, ecosystem recognition, or compatibility with unknown future TSMM/TIS versions.
