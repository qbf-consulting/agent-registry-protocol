# Internet-Draft `-05` Readiness Review (25 October 2026)

**Disposition:** release not yet warranted; preserve published `-04`.  
**Tracking:** [issue #89](https://github.com/qbf-consulting/agent-registry-protocol/issues/89).  
**Immutable IETF reference:** `draft-sankarshan-agent-registry-protocol-04`, published 29 September 2026.  
**Published record:** [Datatracker](https://datatracker.ietf.org/doc/draft-sankarshan-agent-registry-protocol/); [repository submission package](SUBMISSION_PACKAGE_04.md).  
**Comparison:** [post-`-04` changes](https://github.com/qbf-consulting/agent-registry-protocol/compare/132db88f1107b0f97c2a89ba935b16802d56d5c2...main); baseline preparation merge commit `132db88f1107b0f97c2a89ba935b16802d56d5c2`.

## Proposition and acceptance standard

An Internet-Draft revision is warranted by a useful IETF-facing change: an identified protocol-core defect, ambiguity affecting independently interoperable behavior, security or privacy correction, compatibility clarification, or sufficiently consequential editorial improvement. Merely merging repository code, tests, lab documents, operational assurance tools, or research does not establish that condition. The IETF draft is not the full ARPA project specification.

The governing project source remains Candidate v0.10.0 and Candidate amendment PP-04. The published `-04` text remains the IETF protocol comparison baseline; neither is silently overwritten by the other.

## Evidence reviewed

A GitHub compare of the `-04` preparation merge against `main` on 25 October 2026 showed **11 additional commits**. Observed change categories and IETF disposition:

| Change category | Observed evidence | Disposition | Rationale |
|---|---|---|---|
| Agent governance lab, architecture, ADRs, research agenda and experiment guidance | `docs/agent-governance-lab.md`, `docs/architecture/`, `docs/adr/`, `docs/research/` | Project-only | Valuable project and design context, but not a new wire-level contract. |
| External interoperability reporting and validation | `conformance/external/`, `scripts/validate_external_interop.py`, `tests/test_external_interop.py` | Assurance evidence; no promotion | Defines methods for external evidence, not by itself a proven protocol failure or independently reproduced interoperability result. |
| Bounded Rust identifier-resolution experiment | `rust/`, `scripts/run_rust_conformance.py`, `docs/rust-implementation-experiment.md` | Informative; no promotion | Extends repository-controlled implementation diversity; the recorded scope does not establish independent implementation conformance or new normative semantics. |
| Documentation routing and authoring-page corrections | `ietf/index.md`, `docs/publication-map.yml`, `README.md` | Editorial repository correction | No need for a new Datatracker revision. |
| Issue forms, DCO, branch housekeeping and CI | `.github/`, `Makefile` | Repository operations | Outside the IETF protocol core. |
| IETF `-04` publication closeout | `ietf/REVISION_04_CHECKLIST.md`, `ietf/SUBMISSION_PACKAGE_04.md` | Historical publication evidence | Records already-published `-04`, not proposed `-05` semantics. |

The comparison did **not** show a change to `ietf/draft-sankarshan-agent-registry-protocol.md`, `ietf/fragments/revision-04.md`, or a new `spec-delta-v05.yaml`. This is evidence of **no new checked-in IETF proposal**, not a proof that the entire `-04` specification is defect-free.

## Protocol and assurance review

The previous `-04` review classified and addressed identifier ABNF/equality, affirmative authority outcomes, status composition, historical updates, RFC 8785 JSON proof inputs, authority-aware write defaults, cache/freshness limits, idempotency scope, event resynchronization, RFC 9457 errors, critical extensions, SSRF protections, core/profile HTTP boundaries, and discovery separation. See [`REVISION_04_BASELINE.md`](REVISION_04_BASELINE.md) and [`spec-delta-v04.yaml`](spec-delta-v04.yaml).

The post-`-04` change set has not presented a concrete contrary conformance vector, independently observed divergent interpretation, or security defect requiring alteration of those contracts. Those subjects remain legitimate scrutiny targets for future review; they are **not** new accepted `-05` requirements.

Review classification for potential `-05` changes:

- **Accepted new IETF-normative change:** none established by this review.
- **Accepted IETF-informative change:** none requiring immediate publication.
- **Repository-only/editorial:** correct stale `ietf/README.md` publication metadata and authoring instructions.
- **Deferred pending new evidence:** independently reproduced interop differences, material security/privacy defects, ambiguous wire outcomes, and IETF community feedback.
- **Rejected as automatic promotion:** importing project lab, implementation, assurance, A2A/TRQP or deployment material solely because it was added after `-04`.

## Compatibility and authority assessment

No new wire, schema, behavior, authorization, revocation, evidence-interpretation or migration contract is asserted here. No `-05` publication, Internet-Draft status, conformance certification, or independently demonstrated interoperability is claimed. Project-only evidence must not be presented as IETF authority or as an external validation result.

## Documentation correction

`ietf/README.md` had retained `-03` in its current-publication statement, generated-file names, fragment list, and publication-evidence references despite the documented `-04` publication. The correction updates the **current guidance** and adds the `-04` provenance entries; published `-00` through `-04` artifacts remain unchanged.

## Decision and reopening criteria

**Stop at `-04`. Do not prepare or submit `-05` on this evidence.** A follow-up proposal must identify (1) the exact affected published `-04` clause/observable behavior, (2) concrete counterexample or interop/security evidence, (3) proposed normative or editorial disposition, (4) compatibility and migration effects, and (5) conformance or reproducibility evidence. At that point open a governed `-04 → -05` delta and use existing draft-build, rendering, validation and publication checks.

## Validation boundaries

This document records repository-source examination and a GitHub commit/file comparison, **not** a fresh local execution of `make ietf-check` or `make release-check-all`, a new Author Tools review, or new independent interoperable implementation results. No draft publication is performed in this tranche. The previous published `-04` validation and digest evidence remains recorded in [`SUBMISSION_PACKAGE_04.md`](SUBMISSION_PACKAGE_04.md).
