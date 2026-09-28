---
layout: default
title: "Conformance"
nav_exclude: true
---

# Conformance

ARPA conformance is evidence-based across six dimensions: protocol, semantic, cryptographic, operational, governance and enforcement.

- `profiles/` defines Profiles A-D.
- `test-vectors/TV-*` contains the original profile decision vectors.
- `test-vectors/extended/` covers digests, issuer competence, transfer effects, event gaps, aliases, multi-hop delegation, recognition withdrawal and appeal restoration.
- `test-vectors/operational-resilience/` covers retry multiplication, partial outage, event isolation, dependency amplification and sustained-load progress.
- `test-vectors/adversarial/adversarial-authority-v0.9.1.json` covers hostile boundary interpretations of delegation narrowing, time, revocation, source conflict, proof competence, pairwise continuity, historical evidence, `not_applicable`, prohibition inheritance and receipt replay.
- `reports/` contains the implementation-report schema, template and generated reference report.

The v0.9.1 hardening requirement catalogue is `registries/adversarial-hardening-requirements-v0.9.1.json`. It maps the normative hardening amendment to adversarial vectors or explicit inspection evidence. `scripts/validate_candidate_hardening.py` release-gates the catalogue, vector structure and fail-safe outcome constraints.

Run:

```bash
python3 scripts/validate_test_vectors.py
python3 scripts/validate_extended_vectors.py
python3 scripts/validate_candidate_hardening.py
python3 scripts/validate_operational_resilience.py
python3 scripts/generate_implementation_report.py
```

For an ARPA v0.9.1 authority-evaluator claim, the v0.9.0 Candidate Specification and `spec/agent-registry-protocol-v0.9.1-hardening.md` are evaluated together. Passing the adversarial vector structure gate demonstrates that the required hostile cases and prohibited affirmative outcomes are represented; it does not substitute for running those cases against a concrete evaluator or for independent security review.

Operational resilience is cross-cutting and does not create a Profile E. Passing schemas alone is not full ARPA conformance. Implementations must identify unsupported dimensions and operational limitations.


## Authority non-amplification

The Candidate v0.10.0 adversarial corpus includes `conformance/test-vectors/adversarial/authority-laundering-v0.10.0.json`, validating that influence, repetition, reputation, discovery, projection, and unrelated scope do not manufacture authority. See [`docs/authority-non-amplification.md`](../docs/authority-non-amplification.md).
