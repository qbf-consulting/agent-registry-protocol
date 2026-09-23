---
layout: default
title: "Start Here"
nav_exclude: false
nav_order: 2
document_status: informative
permalink: /docs/start-here/
---

# Start here

ARPA is easier to navigate when you begin with the **decision you need to make**, not with the repository directory structure.

## Choose your journey

| You need to… | Go to | Primary outcome |
|---|---|---|
| Understand ARPA's trust and authority model | [1. Understand ARPA](understand.md) | Correct conceptual boundaries and module selection |
| Implement or evaluate code | [2. Build ARPA](build.md) | Working protocol implementation |
| Test a conformance or release claim | [3. Assure & Conform](assure.md) | Machine-verifiable assurance evidence |
| Deploy or govern a registry | [4. Operate ARPA](operate.md) | Operational controls and readiness evidence |
| Connect A2A, TRQP or another system | [5. Integrate & Interoperate](integrate.md) | Explicit protocol-boundary mapping |
| Contribute, release or review governance | [6. Govern & Contribute](govern.md) | Reviewable change-control and repository evidence |

## Version boundary

- **Current normative project baseline:** [ARPA Candidate Specification v0.10.0](../spec/agent-registry-protocol-v0.10.0.md).
- **Historical provenance:** Candidate v0.9.0 plus the adversarial-hardening, PP-01, PP-02 and PP-03 amendment artifacts remain retained for auditability; they are no longer meant to be manually overlaid to determine current requirements.
- **Current implementation release line:** v0.9.5 remains the independently versioned implementation and cross-runtime interoperability release. The GitHub v0.10.0 release is a Candidate Specification consolidation release, not an implementation v0.10.0 claim.

Guides and implementation code do not silently redefine normative requirements. Optional profiles become normative only when that profile is claimed.

## Developer shortcut

If you are here to build something, start with [Build ARPA](build.md), then run `make release-check-all` and review the evidence described in [Assure & Conform](assure.md).

For every rendered document and historical release note, use the [Documentation catalogue](index.md).

## Standards engagement

ARPA maintains a separate IETF Internet-Draft authoring track for the interoperable protocol core. The current published revision is **`draft-sankarshan-agent-registry-protocol-02`**, published on 23 September 2026. It is an independently versioned publication surface and does not replace the ARPA Candidate Specification.

For future `-03` work, use two explicit baselines:

- **IETF comparison baseline:** published `-02`, which is immutable.
- **Current ARPA source baseline:** Candidate v0.10.0, from which protocol-core propositions may be selected through explicit disposition.

Project-only governance, conformance, assurance, deployment and implementation material does not enter a later Internet-Draft automatically.

- [IETF authoring track]({{ '/ietf/' | relative_url }})
- [Protocol extraction map](https://github.com/qbf-consulting/agent-registry-protocol/blob/main/ietf/PROTOCOL_EXTRACTION.md)
- [Published `-02` baseline record](https://github.com/qbf-consulting/agent-registry-protocol/blob/main/ietf/REVISION_02_BASELINE.md)
- [Future `-03` planning](https://github.com/qbf-consulting/agent-registry-protocol/issues/47)

Use this path when reviewing ARPA for IETF protocol extraction, revision deltas, IANA requirements, or overlap with adjacent IETF work.
