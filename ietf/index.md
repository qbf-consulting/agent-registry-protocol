---
layout: default
title: "IETF Internet-Draft Track"
permalink: /ietf/
nav_exclude: true
---

# ARPA IETF Internet-Draft Track

This is the publication landing page for ARPA's **Agent Registry Protocol** Internet-Draft authoring track.

## Current published revision

The current IETF baseline is:

`draft-sankarshan-agent-registry-protocol-02`

It was published on **23 September 2026** as an **Individual Submission** and is **34 pages**.

- [IETF archive](https://www.ietf.org/archive/id/draft-sankarshan-agent-registry-protocol-02.txt)
- [Datatracker status](https://datatracker.ietf.org/doc/draft-sankarshan-agent-registry-protocol/)
- [HTMLized draft](https://datatracker.ietf.org/doc/html/draft-sankarshan-agent-registry-protocol)
- [Diff from the previous revision](https://author-tools.ietf.org/iddiff?url2=draft-sankarshan-agent-registry-protocol-02)

Published `-00` and `-01` remain immutable historical revisions. Future protocol work must start from an explicit `-02 → -03` delta rather than modifying the published `-02` state in place.

## What is standardized here

The IETF track extracts the interoperable protocol core from the broader ARPA Candidate Specification, including:

- the ARPA `agentreg:` Agent Identifier and registry resources;
- typed relationships;
- bounded delegated authority;
- lifecycle and status;
- registration, discovery and current/historical resolution;
- action-specific authority evaluation;
- collective-principal exercise semantics;
- event semantics;
- HTTP processing and RFC 9457 error behavior;
- critical extension and version handling;
- security and privacy considerations;
- composability boundaries with WIMSE, OAuth Token Exchange, RATS and SCITT; and
- IANA actions for protocol identifiers and discovery.

Project governance, conformance programmes, A2A/TRQP profiles, deployment guidance, assurance evidence and redress workflows remain supporting ARPA artifacts unless standardized separately.

## Revision `-02`

Revision `-02` adds explicit action-context binding, exact-action approval semantics, mechanism-neutral collective-principal exercise rules, and stronger standards-context discussion. These changes are governed by Candidate amendment `ARPA-CAND-PP-02` and the `-01 → -02` delta register.

The repository publication evidence is recorded in:

- [Revision `-02` baseline review](REVISION_02_BASELINE.html)
- [Revision `-02` readiness and publication checklist](REVISION_02_CHECKLIST.html)
- [Revision `-02` submission/publication package](SUBMISSION_PACKAGE_02.html)

## Authoring and assurance artifacts

The checked-in base source preserves the historical `-00` authoring baseline. Governed deltas and source fragments deterministically construct later revisions.

- [Internet-Draft base authoring source](draft-sankarshan-agent-registry-protocol.html)
- [Adversarial-hardening source fragment](fragments/adversarial-hardening.html)
- [PP-01 protocol-precision source fragment](fragments/protocol-precision.html)
- [PP-02 authority-at-commitment source fragment](fragments/authority-commitment.html)
- [Rendered `-03` — HTML](generated/draft-sankarshan-agent-registry-protocol-03.html)
- [Rendered `-03` — plaintext](generated/draft-sankarshan-agent-registry-protocol-03.txt)
- [RFCXML v3 for `-03`](generated/draft-sankarshan-agent-registry-protocol-03.xml)
- [Generated-artifact SHA-256 checksums](generated/SHA256SUMS.txt)
- [Protocol extraction and provenance map](PROTOCOL_EXTRACTION.html)
- [Revision `-01` baseline review](REVISION_01_BASELINE.html)
- [Revision `-01` readiness checklist](REVISION_01_CHECKLIST.html)
- [Revision `-02` baseline review](REVISION_02_BASELINE.html)
- [Revision `-02` readiness checklist](REVISION_02_CHECKLIST.html)

## Build, publication and validation

Relevant CI installs the IETF authoring toolchain and executes:

```bash
make ietf-check
```

That gate validates Candidate amendment traceability, IETF authoring inputs and generated `-02` RFCXML/TXT/HTML. GitHub Pages publishes generated artifacts only after publication and link validation succeeds.

Generated outputs remain excluded from Git so they cannot drift as independently committed authority. SHA-256 checksums are published with the rendered artifacts for build evidence.

## Revision `-03` development

Issue **#47** now governs active `-03` preparation. Published `-02` remains the immutable IETF comparison baseline, while Candidate v0.10.0 is the current project source baseline.

The governed `-03` delta includes wire-contract precision, external authority-evidence provenance, TRQP v2.0 composition, optional TSP composition, current WIMSE reference pinning, and evidence-receipt composability. TRQL dependency and TSP VID projection remain deferred.

- [Revision `-03` baseline review](REVISION_03_BASELINE.html)
- [Revision `-03` readiness checklist](REVISION_03_CHECKLIST.html)

The generated `-03` files on this site are **development/submission-preparation artifacts** until IETF publication is independently verified.
