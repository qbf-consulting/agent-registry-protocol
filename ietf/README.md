# ARPA IETF Internet-Draft Track

This directory is the IETF authoring surface for the **Agent Registry Protocol**. It is deliberately separate from the project-level ARPA Candidate Specification.

## Published baseline and active revision

The initial individual Internet-Draft was published by the IETF on **17 September 2026**:

- Published baseline: `draft-sankarshan-agent-registry-protocol-00`
- Title: *Agent Registry Protocol*
- Group: Individual Submission
- Datatracker: <https://datatracker.ietf.org/doc/draft-sankarshan-agent-registry-protocol/>
- Archived text: <https://www.ietf.org/archive/id/draft-sankarshan-agent-registry-protocol-00.txt>
- HTMLized: <https://datatracker.ietf.org/doc/html/draft-sankarshan-agent-registry-protocol>

The IETF archive is the immutable historical authority for revision `-00`. Repository changes after publication do not modify that artifact.

The active repository branch work prepares:

`draft-sankarshan-agent-registry-protocol-01`

Revision `-01` is a candidate until the repository change is reviewed, merged, validated and subsequently submitted to the IETF. The IETF revision series is independent of ARPA implementation-release semantic versions.

## Authority and scope

The ARPA v0.9.0 Candidate Specification remains the normative project baseline. Candidate amendments can refine that baseline without reusing implementation-release version numbers. The Internet-Draft extracts only interoperable protocol-core semantics.

Current IETF-core topics include:

- the ARPA Agent Identifier and registry resources;
- typed relationships;
- bounded delegated authority;
- lifecycle and status;
- registration, discovery and current resolution;
- deterministic point-in-time historical resolution;
- event semantics;
- HTTP processing and RFC 9457 error behavior;
- critical extension/version handling;
- security and privacy considerations; and
- required IANA actions for protocol identifiers/discovery.

Project governance, conformance programmes, A2A/TRQP profiles, deployment guidance, assurance evidence and redress workflows remain supporting ARPA artifacts unless a later revision establishes a concrete interoperability requirement for promotion.

## Revision-control model

The checked-in `ietf/draft-sankarshan-agent-registry-protocol.md` deliberately preserves the published `-00` authoring baseline. Revision `-01` is constructed from explicit governed deltas rather than by silently converting that file into a moving draft.

The `-01` evidence chain is:

```text
published -00 baseline
        ↓
REVISION_01_BASELINE.md
        ↓
spec-delta-v01.yaml
        ↓
ARPA Candidate Protocol Precision Amendment PP-01
        ↓
requirements + conformance vectors
        ↓
IETF protocol-precision fragment / bounded build transforms
        ↓
generated -01 RFCXML / TXT / HTML
```

The accepted `-01` propositions are:

1. `ARPA-IETF-001` — align the IETF Agent Identifier contract with ARPA's `agentreg:` scheme;
2. `ARPA-IETF-002` — make historical resolution a deterministic reconstruction contract;
3. `ARPA-IETF-003` — make RFC 9457 Problem Details the interoperable HTTP error contract for protocol-significant failures; and
4. `ARPA-IETF-004` — define fail-safe processing for unknown material critical extensions.

See:

- `REVISION_01_BASELINE.md` — human-readable review and disposition;
- `spec-delta-v01.yaml` — machine-readable delta register;
- `PROTOCOL_EXTRACTION.md` — project-to-IETF scope and provenance map; and
- `REVISION_01_CHECKLIST.md` — readiness and submission gates.

## Candidate Specification inputs

The IETF track currently consumes protocol-core semantics from:

- `spec/agent-registry-protocol-v0.9.0.md` — Candidate architecture and normative protocol baseline;
- `spec/agent-registry-protocol-v0.9.1-hardening.md` — existing adversarial-authority Candidate amendment; and
- `spec/agent-registry-protocol-protocol-precision-pp01.md` — Candidate Protocol Precision Amendment `ARPA-CAND-PP-01`.

Machine-verifiable evidence for `ARPA-CAND-PP-01` is recorded in:

- `registries/protocol-precision-requirements-pp01.json`;
- `conformance/test-vectors/protocol-precision/protocol-precision-pp01.json`; and
- `artifacts/conformance/protocol-precision-validation.json` when validation runs.

## IETF authoring inputs

The `-01` build consumes:

- `ietf/draft-sankarshan-agent-registry-protocol.md` — retained `-00` authoring baseline;
- `ietf/fragments/adversarial-hardening.md` — protocol-core adversarial hardening;
- `ietf/fragments/protocol-precision.md` — PP-01 protocol-core precision; and
- `scripts/build_ietf_draft.sh` — exact-match transformations for revision identity, `agentreg:` identifier text, RFC 7595 and the corresponding IANA requests.

The build script fails instead of silently applying these transformations if the expected baseline paragraphs no longer match. This makes a change to the historical source shape an explicit review event.

Generated files remain derivative publication artifacts and are excluded from Git as independent normative state.

## Legal status

Files under `ietf/` are prepared as prospective **IETF Contributions**. Submission to the IETF is governed by the IETF Trust Legal Provisions and applicable BCP 78 terms. This does not change the artifact-specific licensing of the existing ARPA project specification, code, schemas, test vectors or documentation.

Do not add a separate CC BY 4.0 notice to the Internet-Draft body or IETF source fragments.

## Build and validation

Install the IETF authoring dependencies:

```bash
make ietf-setup
```

Build RFCXML v3, plaintext and HTML:

```bash
make ietf-build
```

Run the full IETF gate:

```bash
make ietf-check
```

The gate validates PP-01 protocol-precision traceability, IETF source invariants, deterministic `-01` generation and generated output markers. Generated files are written to `ietf/generated/` as:

- `draft-sankarshan-agent-registry-protocol-01.xml`
- `draft-sankarshan-agent-registry-protocol-01.txt`
- `draft-sankarshan-agent-registry-protocol-01.html`

## CI and publication

The dedicated IETF workflow runs when IETF inputs, the PP-01 amendment/evidence, build scripts or the Makefile change. It runs `make ietf-check` and retains the generated `-01` XML/TXT/HTML as an Actions artifact.

The Pages workflow independently runs the same IETF gate before staging the generated `-01` artifacts under `/ietf/generated/`. Complete publication validation and link checking remain required for deployment.

A project-level `spec/` edit does not automatically rewrite IETF protocol text. A protocol-core semantic crosses the boundary only when it is explicitly classified in the delta register and synchronized into the IETF authoring/build surface.

## Historical `-00` evidence

The retained `-00` submission artifacts remain historical evidence and are not repurposed for `-01`:

- `SUBMISSION_CHECKLIST.md`
- `SUBMISSION_PACKAGE.md`
- `SUBMISSION_READINESS_REVIEW.md`
- `SUBMISSION_RUNBOOK.md`

Revision `-01` uses `REVISION_01_CHECKLIST.md` for its own readiness gate.

## Submission discipline

A generated `-01` artifact is not submission-ready merely because it builds. Before upload to Datatracker, the revision must satisfy the automated gates, protocol-semantic diff review, IANA/reference review, and the remaining checks in `REVISION_01_CHECKLIST.md`.
