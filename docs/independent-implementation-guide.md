---
layout: default
title: "Independent Implementation Guide"
nav_exclude: false
document_status: informative
permalink: /docs/independent-implementation-guide/
---

# Independent implementation guide

This guide explains how an external implementer can participate in the ARPA lab without adopting the whole repository or claiming premature conformance.

## Goal

The goal is to make independent implementation evidence cheap enough to produce and precise enough to be useful. An implementation report should help reviewers distinguish:

- implemented behavior;
- intentionally unsupported behavior;
- profile-specific behavior;
- deviations from the Candidate Specification;
- ambiguous requirements that need clarification.

## Minimum useful implementation

A minimum useful implementation should support at least one of the following paths:

| Path | Description |
|---|---|
| Read-only registry | Publishes agent identity, lifecycle state and evidence references without write APIs |
| Discovery registry | Supports controlled discovery while preserving discovery-is-not-authority semantics |
| Authority registry | Resolves authority, delegation and lifecycle state for a bounded domain |
| Federated projection | Consumes or projects selected state from another registry with provenance and competence limits |
| Historical resolver | Reconstructs requested-time state from retained evidence and later material events |

An implementer does not need to implement every ARPA module to provide useful evidence. The implementation report must disclose the supported profile and known limits.

## Evidence package

A useful external report should contain:

1. implementation name, version and operator;
2. implementation type and supported profile;
3. source repository or artifact reference if available;
4. schema version and normative baseline used;
5. test vector results;
6. positive cases passed;
7. negative cases rejected;
8. known deviations;
9. unsupported features;
10. security, key and policy assumptions;
11. evidence retention behavior;
12. statement on whether the implementation was operated independently from this repository.

## Suggested report structure

```markdown
# ARPA implementation report

## Implementation identity

## Operator and independence statement

## Supported profile

## Normative baseline

## Test environment

## Positive vector results

## Negative vector results

## Historical-resolution behavior

## Federation or projection behavior

## Known deviations

## Unsupported features

## Evidence bundle

## Security and privacy notes
```

## Independence language

Use precise independence language. For example:

| Claim | Appropriate when |
|---|---|
| Repository-owned implementation track | The code is maintained in this repository or by the same steward |
| External implementation | The codebase is maintained elsewhere but may still be influenced by ARPA contributors |
| Independently operated implementation | The implementation was deployed, run and reported by a distinct operator |
| Independent conformance evidence | The report and evidence were produced without relying on repository-controlled execution |

The repository-owned Python and TypeScript tracks improve implementation diversity, but they are not external organizational independence evidence.

## Submission path

Use the repository's implementation report issue template when submitting external evidence. Include links to artifacts, reproducibility notes and any cases where ARPA requirements were unclear.

## What not to claim

Do not claim:

- production certification;
- legal authority;
- universal interoperability;
- security review completion;
- external independence;
- profile conformance;

unless the submitted evidence directly supports that claim.

## Lab value

Independent implementation reports are useful even when they fail. Failures reveal ambiguous requirements, unrealistic assumptions, missing vectors and hidden coupling in the reference implementation.
