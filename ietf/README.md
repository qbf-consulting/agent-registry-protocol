# ARPA IETF Internet-Draft Track

This directory is the IETF authoring surface for the **Agent Registry Protocol**. It is deliberately separate from the project-level ARPA Candidate Specification.

## Published revisions and active baseline

The current published Internet-Draft baseline is:

- Current revision: `draft-sankarshan-agent-registry-protocol-02`
- Published: 23 September 2026
- Title: *Agent Registry Protocol*
- Group: Individual Submission
- Pages: 34
- Datatracker: <https://datatracker.ietf.org/doc/draft-sankarshan-agent-registry-protocol/>
- Archived text: <https://www.ietf.org/archive/id/draft-sankarshan-agent-registry-protocol-02.txt>
- HTMLized: <https://datatracker.ietf.org/doc/html/draft-sankarshan-agent-registry-protocol>
- Diff from `-01`: <https://author-tools.ietf.org/iddiff?url2=draft-sankarshan-agent-registry-protocol-02>

Published `-00` and `-01` remain immutable historical revisions. The IETF revision series is independent of ARPA implementation-release semantic versions. Any future protocol change is candidate work for `-03` or later and must be evaluated as an explicit `-02 → -03` delta.

## Authority and scope

The ARPA v0.9.0 Candidate Specification remains the normative project baseline. Candidate amendments refine that baseline without reusing implementation-release version numbers. The Internet-Draft extracts only interoperable protocol-core semantics.

Current IETF-core topics include:

- the ARPA `agentreg:` Agent Identifier and registry resources;
- typed relationships;
- bounded delegated authority;
- lifecycle and status;
- registration, discovery and current resolution;
- deterministic point-in-time historical resolution;
- action-specific authority evaluation;
- collective-principal exercise semantics;
- event semantics;
- HTTP processing and RFC 9457 error behavior;
- critical extension/version handling;
- security and privacy considerations;
- standards-context boundaries with WIMSE, OAuth Token Exchange, RATS and SCITT; and
- required IANA actions for protocol identifiers/discovery.

Project governance, conformance programmes, A2A/TRQP profiles, deployment guidance, assurance evidence and redress workflows remain supporting ARPA artifacts unless a later revision establishes a concrete interoperability requirement for promotion.

## Revision-control model

The checked-in `ietf/draft-sankarshan-agent-registry-protocol.md` deliberately preserves the published `-00` authoring baseline. Later revisions are constructed from explicit governed deltas and bounded transformations rather than by silently converting that file into a moving draft.

Historical revision evidence is recorded in:

- `SUBMISSION_PACKAGE.md` and `SUBMISSION_CHECKLIST.md` for `-00`;
- `REVISION_01_BASELINE.md`, `spec-delta-v01.yaml`, `REVISION_01_CHECKLIST.md`, and `SUBMISSION_PACKAGE_01.md` for `-01`; and
- `REVISION_02_BASELINE.md`, `spec-delta-v02.yaml`, `REVISION_02_CHECKLIST.md`, and `SUBMISSION_PACKAGE_02.md` for `-02`.

The accepted `-01` propositions are:

1. `ARPA-IETF-001` — align the IETF Agent Identifier contract with ARPA's `agentreg:` scheme;
2. `ARPA-IETF-002` — make historical resolution a deterministic reconstruction contract;
3. `ARPA-IETF-003` — make RFC 9457 Problem Details the interoperable HTTP error contract for protocol-significant failures; and
4. `ARPA-IETF-004` — define fail-safe processing for unknown material critical extensions.

The accepted `-02` propositions are:

1. `ARPA-IETF-101` — action-specific authority binding;
2. `ARPA-IETF-102` — collective-principal exercise semantics; and
3. `ARPA-IETF-103` — stronger adjacent-IETF standards context.

## Candidate Specification inputs

The IETF track currently consumes protocol-core semantics from:

- `spec/agent-registry-protocol-v0.9.0.md` — Candidate architecture and normative protocol baseline;
- `spec/agent-registry-protocol-v0.9.1-hardening.md` — adversarial-authority Candidate amendment;
- `spec/agent-registry-protocol-protocol-precision-pp01.md` — Candidate Protocol Precision Amendment `ARPA-CAND-PP-01`; and
- `spec/agent-registry-protocol-authority-commitment-pp02.md` — Candidate Authority-at-Commitment Amendment `ARPA-CAND-PP-02`.

Machine-verifiable evidence is kept alongside the governing amendments in `registries/`, `conformance/test-vectors/`, and repository validation artifacts.

## IETF authoring and build

The current build consumes:

- `ietf/draft-sankarshan-agent-registry-protocol.md` — retained `-00` authoring baseline;
- `ietf/fragments/adversarial-hardening.md`;
- `ietf/fragments/protocol-precision.md`;
- `ietf/fragments/authority-commitment.md`; and
- `scripts/build_ietf_draft.sh`.

The build script uses exact-match transformations and fails instead of silently applying changes when expected historical source markers no longer match.

Install dependencies with:

```bash
make ietf-setup
```

Build RFCXML v3, plaintext and HTML with:

```bash
make ietf-build
```

Run the full IETF gate with:

```bash
make ietf-check
```

The current generated development/publication outputs are:

- `draft-sankarshan-agent-registry-protocol-02.xml`
- `draft-sankarshan-agent-registry-protocol-02.txt`
- `draft-sankarshan-agent-registry-protocol-02.html`

Generated files remain derivative artifacts and are excluded from Git as independent normative state.

## CI and publication

The dedicated IETF workflow runs when governed IETF inputs, Candidate amendment/evidence inputs, build scripts or the Makefile change. It executes `make ietf-check` and retains generated RFCXML/TXT/HTML as an Actions artifact.

The Pages workflow independently runs the IETF gate before staging generated artifacts under `/ietf/generated/`. Complete publication validation and link checking remain required for deployment.

A project-level `spec/` edit does not automatically rewrite IETF protocol text. A protocol-core semantic crosses the boundary only when it is explicitly classified in a revision delta register and synchronized into the IETF authoring/build surface.

## Publication evidence

Revision `-02` is the current published baseline. Its exact governed build state, artifact digests, manual review, and canonical IETF publication references are recorded in `SUBMISSION_PACKAGE_02.md`.

Revision `-01` remains preserved in `SUBMISSION_PACKAGE_01.md`; `-00` evidence remains in the original submission package/checklist/readiness artifacts.

## Submission discipline

Every future revision must repeat the governed baseline/delta, implementation evidence where normative promotion is proposed, rendered-artifact review, IETF submission validation, and publication closeout process. Published `-02` must not be treated as a moving document.

The current future-work tracker for possible `-03` federated trust resolution and TSP/TRQP composability is issue #47.
