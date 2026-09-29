# ARPA Internet-Draft Revision `-04` Submission Package

**Status:** submission-ready candidate; not yet published on the IETF Datatracker  
**Tracking issue:** #65  
**Pull request:** #66  
**Source commit:** `5172da3cf6ee3aff418b6f3e2e6ac12aba9338fe`  
**Published predecessor:** `draft-sankarshan-agent-registry-protocol-03`  
**Target revision:** `draft-sankarshan-agent-registry-protocol-04`

## Governing source

- ARPA Candidate v0.10.0
- ARPA Candidate Protocol Interoperability Amendment `ARPA-CAND-PP-04`
- `ietf/REVISION_04_BASELINE.md`
- `ietf/spec-delta-v04.yaml`
- `ietf/conformance-matrix-v04.json`
- `ietf/fragments/revision-04.md`

Published revision `-03` remains immutable and canonical until the Datatracker accepts `-04`.

## Successful assurance runs

### IETF Internet-Draft

- workflow run: `36525943921`
- result: success
- artifact ID: `11013908173`
- artifact name: `draft-sankarshan-agent-registry-protocol-04`
- artifact archive digest reported by GitHub: `sha256:012d98dd94e797de795d8cc9d0460abf60276991de0be27b5dc8b441069a6082`

The workflow executed the deterministic `make ietf-check` path and successfully rendered RFCXML v3, plaintext, and HTML.

### Full repository validation

- workflow run: `36525943846`
- result: success

The full gate covers repository validation, reference implementation tests, independent TypeScript checks, Python↔TypeScript conformance comparison, network interoperability, and complete GitHub Pages publication/link validation.

## Submission artifacts

| Artifact | SHA-256 |
|---|---|
| `draft-sankarshan-agent-registry-protocol-04.xml` | `b8d40b120094de240c28ac958acf1169c8761d16b0ef6b1bbb211c3afbd8c8e2` |
| `draft-sankarshan-agent-registry-protocol-04.txt` | `f9650805f635ea0fdce64bff6c07dc5ccd7e3ad6e3aac0f7eaf5061f3d4874a0` |
| `draft-sankarshan-agent-registry-protocol-04.html` | `67eb64da20d17d780bfd35bc2ae5e8af3979afbfad7340d403886f1e9be40401` |

The download bundle contains exactly these three files.

## Manual artifact inspection

The rendered plaintext was inspected for the promoted -04 surfaces, including:

- revision-04 hardening section;
- self-contained protocol-core wire structures;
- Authority Evaluation Result wire object;
- `agentreg` ABNF;
- RFC 8785 JCS reference; and
- absence of TODO/FIXME/TBD placeholders.

## Datatracker upload

Use the generated **RFCXML v3** file as the primary revision upload:

`draft-sankarshan-agent-registry-protocol-04.xml`

The TXT and HTML files are deterministic companion renderings for verification and archival evidence.

## Post-submission closeout

After the Datatracker accepts revision `-04`:

1. verify the canonical IETF archive and Datatracker URLs;
2. record the publication timestamp and resulting page count;
3. update `ietf/index.md` so `-04` becomes the published immutable baseline;
4. mark the external-submission gates in `REVISION_04_CHECKLIST.md`;
5. record the accepted publication evidence in this file; and
6. close issue #65 if no residual defects remain.
