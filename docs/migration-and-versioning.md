---
layout: default
title: "Migration and Versioning"
nav_exclude: true
---

# Migration and Versioning

ARPA has distinct version authority surfaces: the Candidate Specification, repository implementation releases, separately versioned schemas, and IETF Internet-Draft revisions. A version advance on one surface does not silently advance another. The current normative project baseline is Candidate v0.10.0; v0.9.5 remains the current implementation-release line, and published IETF `-02` remains the current immutable Internet-Draft baseline.

Record schema versions evolve independently from the specification version. Backward-compatible additions use a minor schema version; incompatible changes use a major version and require migration guidance.

Canonical identifiers are not replaced during schema migration. Supersession links old and new records. Implementations must preserve historical verification material for the published retention period and disclose when reconstruction is incomplete or approximate.
