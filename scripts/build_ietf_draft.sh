#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE="$ROOT/ietf/draft-sankarshan-agent-registry-protocol.md"
HARDENING="$ROOT/ietf/fragments/adversarial-hardening.md"
PRECISION="$ROOT/ietf/fragments/protocol-precision.md"
AUTHORITY="$ROOT/ietf/fragments/authority-commitment.md"
REVISION03="$ROOT/ietf/fragments/revision-03.md"
OUT="$ROOT/ietf/generated"
BASE="draft-sankarshan-agent-registry-protocol-03"
COMBINED="$(mktemp)"
trap 'rm -f "$COMBINED"' EXIT

mkdir -p "$OUT"

if ! command -v kramdown-rfc >/dev/null 2>&1; then
  echo "error: kramdown-rfc is not installed; run 'make ietf-setup'" >&2
  exit 2
fi
if ! command -v xml2rfc >/dev/null 2>&1; then
  echo "error: xml2rfc is not installed; run 'make ietf-setup'" >&2
  exit 2
fi
for fragment in "$HARDENING" "$PRECISION" "$AUTHORITY" "$REVISION03"; do
  if [ ! -f "$fragment" ]; then
    echo "error: missing IETF fragment: $fragment" >&2
    exit 2
  fi
done

python3 - "$SOURCE" "$HARDENING" "$PRECISION" "$AUTHORITY" "$REVISION03" "$COMBINED" <<'PY'
from pathlib import Path
import sys

source = Path(sys.argv[1]).read_text(encoding="utf-8")
hardening = Path(sys.argv[2]).read_text(encoding="utf-8").strip()
precision = Path(sys.argv[3]).read_text(encoding="utf-8").strip()
authority = Path(sys.argv[4]).read_text(encoding="utf-8").strip()
revision03 = Path(sys.argv[5]).read_text(encoding="utf-8").strip()

# The checked-in source preserves the published -00 authoring baseline. The
# -01 build applies only explicit, reviewable transformations plus governed
# protocol-core fragments.
source = source.replace(
    "docname: draft-sankarshan-agent-registry-protocol-00",
    "docname: draft-sankarshan-agent-registry-protocol-03",
    1,
)

source = source.replace(
    '    date: 2026-07-16\n    target: https://qbf-consulting.github.io/agent-registry-protocol/spec/agent-registry-protocol-v0.9.0.html',
    '    date: 2026-09-23\n    target: https://qbfconsulting.digital/agent-registry-protocol/spec/agent-registry-protocol-v0.10.0.html',
    1,
)

# Preserve the published -00 authoring baseline, but do not introduce RFC stream
# metadata in -01 when the existing Datatracker document has no stream recorded.
# This avoids idnits3 SUBMISSION_TYPE_UNEXPECTED on revision upload.
submission_type = "submissiontype: IETF\n"
if submission_type not in source:
    raise SystemExit("error: -00 submissiontype marker changed; review -01 stream-metadata transform")
source = source.replace(submission_type, "", 1)
source = source.replace(
    "  RFC3986:\n  RFC9457:",
    "  RFC3986:\n  RFC6838:\n  RFC7595:\n  RFC8615:\n  RFC9457:",
    1,
)
# RFC8615 is informative in the published -00 source. Revision -01 uses it
# normatively for the well-known URI registration, so move rather than duplicate it.
old_informative = "informative:\n  RFC6749:\n  RFC8414:\n  RFC8615:\n  RFC9421:"
new_informative = "informative:\n  RFC6749:\n  RFC8414:\n  RFC9421:"
if old_informative not in source:
    raise SystemExit("error: -00 informative references changed; review RFC8615 promotion")
source = source.replace(old_informative, new_informative, 1)

expanded_informative = """informative:
  RFC6749:
  RFC8414:
  RFC8693:
  RFC9334:
  RFC9421:
  RFC9943:
  WIMSE-ARCH:
    title: "Workload Identity in a Multi System Environment (WIMSE) Architecture"
    author:
      -
        ins: J. Salowey
        name: Joseph Salowey
    date: 2026-07-06
    target: https://datatracker.ietf.org/doc/draft-ietf-wimse-arch/08/
  WIMSE-CROSS-ORG:
    title: "Cross-Organizational Delegation for Workload and Agent Identity: Problem Statement and Requirements"
    author:
      -
        ins: M. Reece
        name: Morgan Reece
    date: 2026-08-31
    target: https://datatracker.ietf.org/doc/draft-reece-wimse-cross-org-delegation/02/
  TRQP-V2:
    title: "ToIP Trust Registry Query Protocol (TRQP) v2.0"
    author:
      -
        ins: D. O'Donnell
        name: Darrell O'Donnell
      -
        ins: A. Kesselman
        name: Andor Kesselman
      -
        ins: D. Reed
        name: Drummond Reed
    date: 2026
    target: https://github.com/trustoverip/tswg-trust-registry-protocol/tree/main/specification/v2-approved
  TOIP-TSP:
    title: "ToIP Trust Spanning Protocol Specification"
    date: 2026
    target: https://trustoverip.github.io/tswg-tsp-specification/
"""
if new_informative not in source:
    raise SystemExit("error: -01 informative references changed; review -02 reference transform")
source = source.replace(new_informative, expanded_informative.rstrip(), 1)

old_identifier = (
    "An Agent Identifier MUST be a URI conforming to {{RFC3986}}. Its scheme and "
    "dereference behavior are deployment choices unless another specification defines "
    "them. ARPA does not define a new URI scheme in this document."
)
new_identifier = """An Agent Identifier MUST use the `agentreg` URI scheme defined by this document and MUST conform to {{RFC3986}}. The syntax is:

~~~~
agentreg:<registry-namespace>:<agent-local-id>
~~~~

The `registry-namespace` identifies the registry namespace in which the local identifier is assigned. The `agent-local-id` identifies the logical agent within that namespace. Implementations MUST NOT emit a different URI scheme as the ARPA Agent Identifier merely because the agent also has an identifier in another identity or discovery system.

External identifiers MAY be represented as aliases or mapped identifiers, but they MUST remain distinguishable from the ARPA Agent Identifier. A resolver receiving an unsupported identifier scheme MUST NOT silently reinterpret it as an ARPA Agent Identifier; an explicit mapping mechanism MAY be used when the resulting `agentreg` identifier and mapping provenance are preserved."""
if old_identifier not in source:
    raise SystemExit("error: -00 identifier paragraph changed; review the -01 transformation")
source = source.replace(old_identifier, new_identifier, 1)

old_iana = """# IANA Considerations

This document requests no IANA actions in `-00`.

A future revision may request registration of `/.well-known/agent-registry` in the Well-Known URIs registry and may define or request registries for protocol media types, relation types, or error identifiers if interoperability experience shows that centralized registration is warranted."""
new_iana = """# IANA Considerations

## `agentreg` URI Scheme

This document requests permanent registration of the `agentreg` URI scheme in the URI Schemes registry in accordance with {{RFC7595}}.

Scheme name: `agentreg`

Status: Permanent

Applications/protocols that use this scheme: Agent Registry Protocol (ARPA).

Contact: the author of this document.

Change controller: IETF.

References: this document, Identifier Model and Security Considerations.

The scheme-specific syntax is `agentreg:<registry-namespace>:<agent-local-id>`. The scheme identifies an ARPA Agent Identifier; it does not by itself confer authority, recognition, assurance, or permission. Security considerations are described in the Security Considerations section of this document.

## `/.well-known/agent-registry`

This document requests registration of the `agent-registry` well-known URI suffix in the Well-Known URIs registry in accordance with {{RFC8615}}.

URI suffix: `agent-registry`

Change controller: IETF.

Specification document: this document, Registry Metadata.

Related information: the resource identifies ARPA registry metadata and discovery information. A representation SHOULD use a media type appropriate to the selected representation format; JSON deployments SHOULD use `application/json` unless a future specification registers a more specific media type. Access control remains operation-specific, and discovery of this resource does not imply authority, recognition, assurance, endorsement, or permission to invoke any discovered agent.

No IANA registry for project-specific relationship types, extension namespaces, reason codes, or conformance profiles is requested by this revision.

## `application/agent-registry+json` Media Type

This document requests registration of the media type `application/agent-registry+json` in accordance with {{RFC6838}}.

Type name: application

Subtype name: agent-registry+json

Required parameters: none

Optional parameters: none

Encoding considerations: binary; JSON representations use UTF-8 as required by {{RFC8259}}.

Security considerations: see the Security Considerations and Privacy Considerations sections of this document. ARPA representations can expose authority, relationship, lifecycle, endpoint, and evidence information and therefore can be security- and privacy-sensitive.

Interoperability considerations: protocol/profile versioning is carried in ARPA metadata and representations, not inferred from a media-type version parameter. `application/json` may be supported only as a semantics-identical compatibility fallback.

Published specification: this document.

Applications that use this media type: Agent Registry Protocol implementations.

Fragment identifier considerations: none defined by this document.

Additional information: none.

Person and email address to contact for further information: the author of this document.

Intended usage: COMMON

Restrictions on usage: none.

Author: the author of this document.

Change controller: IETF."""

if old_iana not in source:
    raise SystemExit("error: -00 IANA section changed; review the -01 transformation")
source = source.replace(old_iana, new_iana, 1)

old_changelog = """## -00

* Initial individual submission extracted from the ARPA Candidate Specification and implementation corpus.
* Defines HTTP/JSON registry metadata, agent/deployment resources, relationships, authority envelopes, lifecycle/status handling, current and historical resolution, discovery, events, errors, versioning, security, privacy, operations, and conformance."""
new_changelog = old_changelog + """

## -01
{: #revision-01}

* Aligns the ARPA Agent Identifier with the `agentreg:` scheme already used by the Candidate Specification and machine-readable API contract.
* Adds adversarial authority-processing requirements for monotonic delegation, temporal boundaries, conflict handling, revocation effectiveness, decision reproducibility, and proof-input semantics.
* Defines deterministic historical-resolution reconstruction, RFC 9457 Problem Details behavior, and fail-safe critical-extension processing.
* Requests IANA registration of the `agentreg` URI scheme and the `agent-registry` well-known URI suffix.
* Preserves project governance, A2A, TRQP, assurance-profile, and redress semantics outside the IETF protocol core.

## -02
{: #revision-02}

* Defines action-specific authority evaluation with explicit action context, current-authority checks, constraint preservation, and exact-action approval binding.
* Defines mechanism-neutral collective-principal exercise semantics, including current membership/rule evidence and distinct-controller threshold counting.
* Strengthens composability guidance and informative references for WIMSE workload identity/delegation, OAuth 2.0 Token Exchange, RATS attestation, and SCITT transparency.
* Preserves the separation between registry-visible authority evidence and the relying party's final authorization or execution decision.

## -03
{: #revision-03}

* Defines interoperable authority-evaluation outcome semantics, including a machine-stable `not_applicable` boundary distinct from protocol errors, deny, and indeterminate.
* Adds explicit parent-authority linkage, lower-bound time semantics, discoverable clock-profile assumptions, and collective-principal snapshot binding.
* Registers `application/agent-registry+json` and tightens RFC 9457 Problem Details and extension-namespace processing.
* Defines how external authoritative trust evidence contributes to ARPA evaluation and specifies normative composition boundaries with ToIP TRQP v2.0.
* Describes ToIP TSP as an optional spanning substrate without making TSP a conformance dependency and preserves the rule that authenticated channels/identifiers do not confer authority.
* Pins WIMSE references to the revisions reviewed for this draft and clarifies optional SCITT evidence-reference composition.
* Makes IETF-draft precedence explicit for IETF protocol conformance while retaining Candidate v0.10.0 as the project baseline for wider governance/profile material."""

if old_changelog not in source:
    raise SystemExit("error: -00 changelog changed; review the -01 changelog transformation")
source = source.replace(old_changelog, new_changelog, 1)

fragments = f"{hardening}\n\n{precision}\n\n{authority}\n\n{revision03}"
unnumbered = "\n# Acknowledgements\n{:unnumbered}\n"
numbered = "\n# Acknowledgements\n"
if unnumbered in source:
    combined = source.replace(
        unnumbered,
        f"\n\n{fragments}\n\n# Acknowledgements\n{{:unnumbered}}\n",
        1,
    )
elif numbered in source:
    combined = source.replace(
        numbered,
        f"\n\n{fragments}\n\n# Acknowledgements\n",
        1,
    )
else:
    raise SystemExit("error: IETF source is missing the Acknowledgements marker")

Path(sys.argv[6]).write_text(combined, encoding="utf-8")
PY

kramdown-rfc "$COMBINED" > "$OUT/$BASE.xml"

if grep -q 'submissionType=' "$OUT/$BASE.xml"; then
  echo "error: generated -03 RFCXML unexpectedly contains submissionType metadata" >&2
  exit 2
fi

xml2rfc --text --out "$OUT/$BASE.txt" "$OUT/$BASE.xml"
xml2rfc --html --out "$OUT/$BASE.html" "$OUT/$BASE.xml"

echo "Built revision -03 from:"
echo "  ietf/draft-sankarshan-agent-registry-protocol.md (-00 authoring baseline)"
echo "  ietf/fragments/adversarial-hardening.md"
echo "  ietf/fragments/protocol-precision.md"
echo "  ietf/fragments/authority-commitment.md"
echo "  ietf/fragments/revision-03.md"
echo "Built:"
echo "  ietf/generated/$BASE.xml"
echo "  ietf/generated/$BASE.txt"
echo "  ietf/generated/$BASE.html"
