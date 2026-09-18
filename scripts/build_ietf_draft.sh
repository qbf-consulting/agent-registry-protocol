#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE="$ROOT/ietf/draft-sankarshan-agent-registry-protocol.md"
HARDENING="$ROOT/ietf/fragments/adversarial-hardening.md"
PRECISION="$ROOT/ietf/fragments/protocol-precision.md"
OUT="$ROOT/ietf/generated"
BASE="draft-sankarshan-agent-registry-protocol-01"
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
for fragment in "$HARDENING" "$PRECISION"; do
  if [ ! -f "$fragment" ]; then
    echo "error: missing IETF fragment: $fragment" >&2
    exit 2
  fi
done

python3 - "$SOURCE" "$HARDENING" "$PRECISION" "$COMBINED" <<'PY'
from pathlib import Path
import sys

source = Path(sys.argv[1]).read_text(encoding="utf-8")
hardening = Path(sys.argv[2]).read_text(encoding="utf-8").strip()
precision = Path(sys.argv[3]).read_text(encoding="utf-8").strip()

# The checked-in source preserves the published -00 authoring baseline. The
# -01 build applies only explicit, reviewable transformations plus governed
# protocol-core fragments.
source = source.replace(
    "docname: draft-sankarshan-agent-registry-protocol-00",
    "docname: draft-sankarshan-agent-registry-protocol-01",
    1,
)
source = source.replace(
    "  RFC3986:\n  RFC9457:",
    "  RFC3986:\n  RFC7595:\n  RFC8615:\n  RFC9457:",
    1,
)
# RFC8615 is informative in the published -00 source. Revision -01 uses it
# normatively for the well-known URI registration, so move rather than duplicate it.
old_informative = "informative:\n  RFC6749:\n  RFC8414:\n  RFC8615:\n  RFC9421:"
new_informative = "informative:\n  RFC6749:\n  RFC8414:\n  RFC9421:"
if old_informative not in source:
    raise SystemExit("error: -00 informative references changed; review RFC8615 promotion")
source = source.replace(old_informative, new_informative, 1)

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

No IANA registry for project-specific relationship types, extension namespaces, reason codes, or conformance profiles is requested by this revision."""
if old_iana not in source:
    raise SystemExit("error: -00 IANA section changed; review the -01 transformation")
source = source.replace(old_iana, new_iana, 1)

fragments = f"{hardening}\n\n{precision}"
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

Path(sys.argv[4]).write_text(combined, encoding="utf-8")
PY

kramdown-rfc "$COMBINED" > "$OUT/$BASE.xml"
xml2rfc --text --out "$OUT/$BASE.txt" "$OUT/$BASE.xml"
xml2rfc --html --out "$OUT/$BASE.html" "$OUT/$BASE.xml"

echo "Built revision -01 from:"
echo "  ietf/draft-sankarshan-agent-registry-protocol.md (-00 authoring baseline)"
echo "  ietf/fragments/adversarial-hardening.md"
echo "  ietf/fragments/protocol-precision.md"
echo "Built:"
echo "  ietf/generated/$BASE.xml"
echo "  ietf/generated/$BASE.txt"
echo "  ietf/generated/$BASE.html"
