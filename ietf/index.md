---
layout: default
title: "IETF Internet-Draft Track"
permalink: /ietf/
nav_exclude: true
---

# ARPA IETF Internet-Draft Track

This is the publication landing page for ARPA's **Agent Registry Protocol** Internet-Draft authoring track.

## Current state

The published IETF baseline is:

`draft-sankarshan-agent-registry-protocol-00`

It was published on **17 September 2026** and remains the immutable historical `-00` artifact.

The repository is now developing the next candidate revision:

`draft-sankarshan-agent-registry-protocol-01`

The generated `-01` files on this site are **development artifacts**, not evidence that revision `-01` has been submitted, adopted, or approved by the IETF.

## What is standardized here

The IETF track extracts the interoperable protocol core from the broader ARPA Candidate Specification:

- the ARPA `agentreg:` Agent Identifier and registry resources;
- typed relationships;
- bounded delegated authority;
- lifecycle and status;
- registration, discovery and current resolution;
- deterministic point-in-time historical resolution;
- event semantics;
- HTTP processing and RFC 9457 error behavior;
- critical extension and version handling;
- security and privacy considerations; and
- prospective IANA actions.

The v0.9.1 adversarial-hardening rules preserve monotonic delegation, temporal boundaries, non-applicability, authoritative conflict, revocation effectiveness, decision reproducibility and proof-input semantics. The v0.9.2 protocol-precision amendment resolves identifier, historical-resolution, HTTP error and critical-extension ambiguity exposed during the `-01` baseline review.

Project governance, conformance programmes, A2A/TRQP profiles, deployment guidance, assurance evidence and redress workflows remain supporting ARPA artifacts unless standardized separately.

## Authoring and assurance artifacts

The checked-in base source deliberately preserves the published `-00` authoring baseline. The build constructs `-01` from governed deltas, the hardening and precision fragments, and bounded exact-match transformations.

- [Internet-Draft base authoring source](draft-sankarshan-agent-registry-protocol.html)
- [v0.9.1 protocol-hardening source fragment](fragments/adversarial-hardening.html)
- [v0.9.2 protocol-precision source fragment](fragments/protocol-precision.html)
- [Rendered `-01` — HTML](generated/draft-sankarshan-agent-registry-protocol-01.html)
- [Rendered `-01` — plaintext](generated/draft-sankarshan-agent-registry-protocol-01.txt)
- [RFCXML v3 for `-01`](generated/draft-sankarshan-agent-registry-protocol-01.xml)
- [Generated-artifact SHA-256 checksums](generated/SHA256SUMS.txt)
- [Protocol extraction and provenance map](PROTOCOL_EXTRACTION.html)
- [Revision `-01` baseline review](REVISION_01_BASELINE.html)
- [Revision `-01` readiness checklist](REVISION_01_CHECKLIST.html)
- [Repository authoring guide](README.html)

The machine-readable `ietf/spec-delta-v01.yaml` records the accepted and excluded `-00 → -01` propositions.

## Accepted `-01` precision work

The current `-01` candidate intentionally limits change to four protocol propositions:

1. align the IETF Agent Identifier contract with the ARPA `agentreg:` identifier;
2. define historical resolution as deterministic reconstruction rather than timestamp-filtered current state;
3. make RFC 9457 Problem Details the interoperable HTTP error envelope for protocol-significant failures; and
4. require fail-safe handling of unsupported material critical extensions.

The repository intentionally does **not** promote ARPA governance/redress, A2A, TRQP or project assurance-profile semantics into this revision.

## Build, publication and validation

Every relevant CI run installs the IETF authoring toolchain and executes:

```bash
make ietf-check
```

That gate validates the protocol-precision traceability, IETF authoring inputs and generated `-01` RFCXML/TXT/HTML. GitHub Pages publishes the generated artifacts only after its complete publication and link validation succeeds.

Generated outputs remain excluded from Git so they cannot drift as independently committed authority. SHA-256 checksums are published with the rendered artifacts for build evidence.

A successful build is necessary but not sufficient for submission. The remaining semantic-diff and IETF submission hygiene gates are tracked in the revision `-01` checklist.
