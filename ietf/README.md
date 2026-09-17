# ARPA IETF Internet-Draft Track

This directory is the IETF authoring surface for the **Agent Registry Protocol**.
It is deliberately separate from the project-level ARPA Candidate Specification.

## Published draft

The initial individual Internet-Draft was published by the IETF on **17 September 2026**:

- Draft: `draft-sankarshan-agent-registry-protocol-00`
- Title: *Agent Registry Protocol*
- Group: Individual Submission
- Datatracker: <https://datatracker.ietf.org/doc/draft-sankarshan-agent-registry-protocol/>
- Archived text: <https://www.ietf.org/archive/id/draft-sankarshan-agent-registry-protocol-00.txt>
- HTMLized: <https://datatracker.ietf.org/doc/html/draft-sankarshan-agent-registry-protocol>

The IETF archive is the immutable historical authority for revision `-00`. Repository changes after publication do not modify that published artifact; changes to the checked-in IETF source represent development toward `-01` or a later revision and must be recorded accordingly.

## Draft identity

Published individual draft:

`draft-sankarshan-agent-registry-protocol-00`

The IETF draft revision is independent of ARPA project semantic versions. A future
working-group adoption would normally create a new `draft-ietf-<wg>-...-00`
series rather than continuing the individual-draft revision number.

## Authority and scope

The ARPA Candidate Specification remains the project-level specification and
source architecture. The Internet-Draft extracts the interoperable protocol core:

- identifiers and registry resources;
- typed relationships;
- bounded delegated authority;
- lifecycle and status;
- registration and resolution;
- point-in-time resolution;
- event semantics;
- HTTP processing and errors;
- versioning/extensibility;
- security and privacy considerations; and
- prospective IANA actions.

Project governance, conformance programmes, A2A/TRQP profiles, deployment
guidance, and assurance evidence remain supporting ARPA artifacts unless later
standardized separately.

ARPA v0.9.1 adversarial hardening changes that affect the interoperable protocol
core are included in the generated Internet-Draft through the checked-in source
fragment `ietf/fragments/adversarial-hardening.md`. The fragment covers delegation
scope intersection, time boundaries, non-applicability, recognition conflicts,
revocation/effectiveness, decision reproducibility and proof-input semantics.
It is inserted before the Internet-Draft back matter by the deterministic build
script and therefore becomes part of the generated RFCXML/TXT/HTML publication.

## Legal status

Files under `ietf/` are prepared as prospective **IETF Contributions**. Submission
to the IETF is governed by the IETF Trust Legal Provisions and applicable BCP 78
terms. This does not change the artifact-specific licensing of the existing ARPA
project specification, code, schemas, test vectors, or documentation.

Do not add a separate CC BY 4.0 notice to the Internet-Draft body or IETF source
fragments.

## Build

Install the IETF authoring dependencies:

```bash
make ietf-setup
```

Build RFCXML v3, plaintext, and HTML:

```bash
make ietf-build
```

Validate the source and generated RFCXML:

```bash
make ietf-check
```

Generated files are written to `ietf/generated/`.

## Generated artifact policy

The checked-in IETF authoring source set consists of:

- `ietf/draft-sankarshan-agent-registry-protocol.md` — the base individual-draft source; and
- `ietf/fragments/adversarial-hardening.md` — the v0.9.1 protocol-hardening source fragment.

`scripts/build_ietf_draft.sh` deterministically inserts the hardening fragment
before the draft back matter and then produces RFCXML v3, plaintext, and HTML.
Those generated files and any derived PDF remain excluded from Git by
`ietf/.gitignore`.

GitHub Actions owns generation and publication of the submission renderings:

1. the dedicated IETF workflow runs `make ietf-check` on every push or PR touching
   `ietf/**`, the IETF build/validation scripts, the Makefile, or the workflow itself;
2. the workflow retains generated XML, TXT, and HTML as an Actions artifact for
   CI inspection;
3. the GitHub Pages workflow independently runs the same IETF validation gate;
4. a successful Pages build publishes XML, TXT, HTML, the local RFC stylesheet
   hook, and SHA-256 checksums under `/ietf/generated/`;
5. the checksum file is copied into the Pages assurance artifact so published
   outputs can be tied to retained deployment evidence; and
6. a failed IETF build or failed complete-publication validation blocks Pages
   deployment.

This means generated IETF content is automatically regenerated whenever an IETF
source or build input changes. A change only to a project-level `spec/` file does
**not** automatically rewrite the IETF authoring source; protocol-core changes
must be explicitly synchronized into the IETF source set. The v0.9.1 hardening
work does that through the checked-in hardening fragment.

This keeps generated content reproducible and developer-accessible without
allowing generated files to drift as independently committed repository state.
The generated artifacts are publication products, not a separate authority
surface.

## Revision management after `-00`

The published `-00` document is a fixed external baseline. After publication:

1. record review feedback as repository issues with a clear disposition;
2. change the checked-in IETF source only through reviewable commits and pull requests;
3. treat substantive source changes as candidate material for `-01` or later;
4. maintain traceability from each normative change to the issue, rationale, tests/evidence, and target I-D revision; and
5. never describe repository-only edits as modifications to the archived `-00` document.

## Pre-submission gates

The `-00` submission gates were completed before publication. The retained checklist and package evidence remain in:

- `SUBMISSION_CHECKLIST.md`
- `SUBMISSION_PACKAGE.md`
- `SUBMISSION_READINESS_REVIEW.md`
- `SUBMISSION_RUNBOOK.md`

## Version provenance

The published `-00` is derived from the ARPA v0.9.x repository state and the v0.9.0
Candidate Specification baseline, including the v0.9.1 adversarial-hardening
amendment where its semantics belong to the interoperable protocol core. The I-D
MUST NOT silently track a moving `Unreleased` state. Any normative change imported
from ARPA must be reviewed, represented in the checked-in IETF source set, and
recorded in the I-D change history before a subsequent submission.
