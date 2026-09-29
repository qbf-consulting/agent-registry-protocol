# Internet-Draft Revision `-04` Checklist

## Baseline and governance
- [x] Published -03 identified as immutable baseline
- [x] Candidate v0.10.0 retained as current consolidated Candidate baseline
- [x] Candidate PP-04 records Candidate-first semantic hardening
- [x] Every OPEN/PARTIAL finding in #65 has an explicit disposition
- [x] Breaking/potentially-breaking propositions classified
- [x] Machine-readable -04 delta register recorded

## Protocol substance
- [x] Candidate↔IETF field-name mapping defined
- [x] Authority Evaluation Result wire contract defined
- [x] affirmative/non-affirmative grouping made explicit
- [x] multi-dimensional status composition made fail-safe
- [x] agentreg ABNF/equality/normalization defined
- [x] RFC 8785 default JSON canonicalization defined
- [x] freshness and cache bounds defined
- [x] registration retry behavior made deterministic
- [x] PUT replacement/version/precondition semantics defined
- [x] event ordering/gap/resynchronization semantics defined
- [x] write authorization default-deny rule defined
- [x] critical-extension terminology unified
- [x] SSRF/dereference safeguards defined
- [x] registry discovery separated from agent search
- [x] HTTP core/profile operation boundary clarified

## Build and assurance
- [ ] `make ietf-check` passes for -04
- [ ] full Validate workflow passes
- [ ] dedicated IETF workflow passes
- [ ] generated RFCXML v3 reviewed
- [ ] generated plaintext reviewed
- [ ] generated HTML reviewed
- [ ] no TODO/FIXME/TBD/placeholders
- [ ] -03 → -04 rendered semantic diff reviewed
- [ ] exact artifact SHA-256 digests recorded
- [ ] download-ready ZIP produced

## External submission
- [ ] current Author Tools / submission checks completed
- [ ] RFCXML v3 uploaded as revision -04
- [ ] Datatracker publication verified
- [ ] repository publication closeout updated
