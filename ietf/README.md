# ARPA IETF Internet-Draft Track

This directory is the IETF authoring surface for the **Agent Registry Protocol**. It is deliberately separate from the project-level ARPA Candidate Specification.

## Published revisions and active baseline

The current published Internet-Draft baseline is:

- Current revision: `draft-sankarshan-agent-registry-protocol-03`
- Published: 28 September 2026
- Title: *Agent Registry Protocol*
- Group: Individual Submission
- Pages: 44
- Datatracker: <https://datatracker.ietf.org/doc/draft-sankarshan-agent-registry-protocol/>
- Archived text: <https://www.ietf.org/archive/id/draft-sankarshan-agent-registry-protocol-03.txt>
- HTMLized: <https://datatracker.ietf.org/doc/html/draft-sankarshan-agent-registry-protocol>
- Diff from `-02`: <https://author-tools.ietf.org/iddiff?url2=draft-sankarshan-agent-registry-protocol-03>

Published `-00`, `-01`, and `-02` remain immutable historical revisions. The IETF revision series is independent of ARPA Candidate/implementation semantic versions. Future protocol changes must be evaluated as an explicit delta from published `-03`.

## Authority and scope

ARPA Candidate v0.10.0 is the current normative project baseline. The Internet-Draft extracts only interoperable protocol-core semantics, and published `-03` is the current immutable IETF baseline.

Current IETF-core topics include:

- the ARPA `agentreg:` Agent Identifier and registry resources;
- typed relationships and bounded delegated authority;
- lifecycle and current/historical resolution;
- action-specific authority evaluation;
- authority-evaluation outcomes including `not_applicable`;
- parent-authority linkage;
- temporal precision and collective-principal snapshot semantics;
- external authoritative-evidence provenance;
- TRQP v2.0 composition boundaries;
- optional/non-conferring TSP composition;
- event semantics;
- HTTP/RFC 9457 error behavior;
- `application/agent-registry+json`;
- critical extension/version handling;
- security and privacy considerations;
- WIMSE/SCITT composability boundaries; and
- IANA actions for protocol identifiers, discovery, and media type.

Project governance, A2A profiles, deployment guidance, assurance scoring, redress workflows, TRQL dependency, and TSP VID projection remain outside the published IETF core unless promoted through a later governed delta.

## Revision-control model

The checked-in `ietf/draft-sankarshan-agent-registry-protocol.md` deliberately preserves the published `-00` authoring baseline. Later revisions are constructed from explicit governed deltas and bounded transformations.

Historical revision evidence is recorded in:

- `SUBMISSION_PACKAGE.md` and `SUBMISSION_CHECKLIST.md` for `-00`;
- `REVISION_01_BASELINE.md`, `spec-delta-v01.yaml`, `REVISION_01_CHECKLIST.md`, and `SUBMISSION_PACKAGE_01.md` for `-01`;
- `REVISION_02_BASELINE.md`, `spec-delta-v02.yaml`, `REVISION_02_CHECKLIST.md`, and `SUBMISSION_PACKAGE_02.md` for `-02`; and
- `REVISION_03_BASELINE.md`, `spec-delta-v03.yaml`, `REVISION_03_CHECKLIST.md`, and `SUBMISSION_PACKAGE_03.md` for `-03`.

For future work, **published `-03` is the IETF comparison baseline while Candidate v0.10.0 is the current ARPA source baseline**. No Candidate clause enters a later Internet-Draft without explicit IETF delta disposition.

## IETF authoring and build

The current build consumes:

- `ietf/draft-sankarshan-agent-registry-protocol.md` — retained `-00` authoring baseline;
- `ietf/fragments/adversarial-hardening.md`;
- `ietf/fragments/protocol-precision.md`;
- `ietf/fragments/authority-commitment.md`;
- `ietf/fragments/revision-03.md`; and
- `scripts/build_ietf_draft.sh`.

Install dependencies with:

```bash
make ietf-setup
```

Build and validate with:

```bash
make ietf-check
```

The current generated outputs are:

- `draft-sankarshan-agent-registry-protocol-03.xml`
- `draft-sankarshan-agent-registry-protocol-03.txt`
- `draft-sankarshan-agent-registry-protocol-03.html`

Generated files remain derivative artifacts and are excluded from Git as independent normative state.

## Publication evidence

Revision `-03` is the current published baseline. Its governed build state, artifact digests, manual review, and canonical IETF publication references are recorded in `SUBMISSION_PACKAGE_03.md`.

Revision `-02` remains preserved in `SUBMISSION_PACKAGE_02.md`; earlier evidence remains in the corresponding historical submission packages/checklists.

## Submission discipline

Every future revision must repeat the governed baseline/delta, implementation evidence where normative promotion is proposed, rendered-artifact review, IETF submission validation, and publication closeout process. Published `-03` must not be treated as a moving document.
