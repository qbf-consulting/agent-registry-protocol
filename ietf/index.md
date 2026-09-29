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

`draft-sankarshan-agent-registry-protocol-04`

It was published on **29 September 2026** as an **Individual Submission** and is **56 pages**.

- [IETF archive](https://www.ietf.org/archive/id/draft-sankarshan-agent-registry-protocol-04.txt)
- [Datatracker status](https://datatracker.ietf.org/doc/draft-sankarshan-agent-registry-protocol/)
- [HTMLized draft](https://datatracker.ietf.org/doc/html/draft-sankarshan-agent-registry-protocol)
- [Diff from revision `-02`](https://author-tools.ietf.org/iddiff?url2=draft-sankarshan-agent-registry-protocol-04)

Published `-00` through `-03` remain immutable historical revisions. Future protocol work must begin from a governed delta against published `-04`.

## What is standardized here

The IETF track extracts the interoperable protocol core from the broader ARPA Candidate Specification, including:

- the ARPA `agentreg:` Agent Identifier and registry resources;
- typed relationships and bounded delegated authority;
- lifecycle and current/historical resolution;
- action-specific authority evaluation;
- authority-evaluation outcomes including `not_applicable`;
- parent-authority linkage;
- temporal and collective-principal snapshot semantics;
- external authoritative-evidence provenance;
- ToIP TRQP v2.0 composition boundaries;
- optional/non-conferring ToIP TSP composition;
- event semantics;
- HTTP/RFC 9457 error behavior;
- `application/agent-registry+json`;
- critical extension and version handling;
- security and privacy considerations;
- WIMSE/SCITT composability boundaries; and
- current IANA requests.

Project governance, conformance programmes, A2A profiles, deployment guidance, assurance scoring, redress workflows, TRQL dependency, and TSP VID projection remain supporting/project material unless standardized separately.

## Revision `-04`

Revision `-04` adds protocol-interoperability and security hardening, including explicit wire contracts, authority-evaluation outcomes, fail-safe status composition, identifier normalization, freshness/cache rules, deterministic update/event semantics, write authorization, critical-extension handling, SSRF protections, and discovery/search boundaries.

The repository publication evidence is recorded in:

- [Revision `-04` baseline review](REVISION_04_BASELINE.html)
- [Revision `-04` readiness and publication checklist](REVISION_04_CHECKLIST.html)
- [Revision `-04` submission/publication package](SUBMISSION_PACKAGE_04.html)

## Authoring and assurance artifacts

The checked-in base source preserves the historical `-00` authoring baseline. Governed deltas and source fragments deterministically construct later revisions.

- [Internet-Draft base authoring source](draft-sankarshan-agent-registry-protocol.html)
- [Adversarial-hardening source fragment](fragments/adversarial-hardening.html)
- [PP-01 protocol-precision source fragment](fragments/protocol-precision.html)
- [PP-02 authority-at-commitment source fragment](fragments/authority-commitment.html)
- [Revision `-03` source fragment](fragments/revision-03.html)
- [Generated-artifact SHA-256 checksums](generated/SHA256SUMS.txt)
- [Protocol extraction and provenance map](PROTOCOL_EXTRACTION.html)
- [Revision `-03` baseline review](REVISION_03_BASELINE.html)
- [Revision `-03` readiness checklist](REVISION_03_CHECKLIST.html)
## Build, publication and validation

Relevant CI installs the IETF authoring toolchain and executes:

```bash
make ietf-check
```

That gate validates Candidate traceability, IETF authoring inputs and generated current-candidate RFCXML/TXT/HTML. GitHub Pages publishes generated artifacts only after publication and link validation succeeds.

Generated outputs remain excluded from Git so they cannot drift as independently committed authority. SHA-256 checksums are published with the rendered artifacts for build evidence.

## Publication state

Revision `-04` is **published** and is the immutable baseline for future IETF revision work. Repository-generated files are reproducibility artifacts; the canonical historical publication is the IETF archive copy linked above.
