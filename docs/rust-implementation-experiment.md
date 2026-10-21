---
layout: default
title: "Rust Identifier-Resolution Experiment"
nav_exclude: true
document_status: informative
---

# Rust identifier-resolution experiment

## Decision

Retain the Rust implementation as a **bounded informative example and
cross-runtime assurance surface**, provided repository CI remains green.

Do not promote it to a general ARPA Rust SDK, production implementation, or
replacement for the Python and TypeScript tracks. Expansion requires a
separately scoped proposal with evidence that the additional maintenance cost
is justified.

## Hypothesis

A third implementation of one stable ARPA operation can test whether the
shared contract is independently implementable without creating a language
migration programme.

The useful outcome is specification and interoperability evidence. Raw
performance or compile-time type safety is not, by itself, sufficient reason
to maintain another runtime.

## Phase 0 baseline

The selected operation is **Profile A identifier resolution** as exercised by
Candidate v0.10.0 §12.6 behavior and the existing `TV-A-01..03` vectors.

Existing implementations:

| Runtime | Behavioral source | Shared vectors |
|---|---|---|
| Python | `scripts/reference_evaluator.py::resolve_identifier` | `TV-A-01..03` |
| TypeScript | `typescript/src/resolution.ts::resolveIdentifier` | `TV-A-01..03` |
| Rust experiment | `rust/src/lib.rs::resolve_identifier` | `TV-A-01..03` |

The Rust implementation does not import behavioral implementation code from
Python or TypeScript. All three tracks share the governed test vectors.

## Observable contract

The bounded cases establish:

1. a known, active identifier resolves as `active_record`;
2. a never-issued identifier resolves as `not_found`;
3. a known terminal identifier resolves as `terminal_record` and is not
   masked as unknown;
4. an unauthorized known identifier is represented separately by the Rust
   unit boundary test as `not_authorized`.

Resolution is a registry fact, not an authorization decision. The experiment
does not infer recognition, trust, capability, or permission from successful
resolution.

## Reproduction

```bash
cargo test --manifest-path rust/Cargo.toml
python3 scripts/run_rust_conformance.py
make cross-runtime
```

`make rust-check` executes the Rust tests and shared-vector harness.
`make release-check-all` includes the Rust experiment before cross-runtime
comparison.

Generated evidence:

```text
artifacts/rust/conformance-report.json
artifacts/typescript/cross-runtime-report.json
```

CI uploads the Rust report as part of the candidate interoperability evidence.

## Evidence interpretation

For Profile A identifier-resolution vectors, cross-runtime equivalence requires
the Python, TypeScript, and Rust outcomes to equal the shared expected outcome.

For authority-evaluation vectors, the Rust experiment is explicitly recorded
as `not_in_experiment_scope`; those vectors continue to compare Python and
TypeScript only. Unsupported behavior is not represented as PASS.

## Dependency, packaging, and maintenance assessment

The Rust crate uses only the standard library and produces a standalone binary
for the selected operation. This avoids a third-party Rust dependency graph.

The maintenance cost is still non-zero:

- one additional toolchain is exercised in CI;
- fixture and cross-runtime harnesses must remain aligned;
- documentation must preserve the experimental boundary;
- future protocol changes affecting §12.6 must update three runtime tracks.

For this bounded slice, the extra cost is justified because it adds a third
behaviorally independent implementation with very little code and no new
protocol semantics. That evidence does **not** justify rewriting the Python
implementation or expanding Rust automatically.

## Disposition

**Retain as informative example.**

The experiment should remain deliberately small. A future expansion is
warranted only if it targets a consequential stable contract and is expected
to expose ambiguity, improve deployment portability, or add material
conformance evidence that cannot be obtained more cheaply from the existing
tracks.

No implementation release or Candidate Specification version change is
required solely for this experiment.
