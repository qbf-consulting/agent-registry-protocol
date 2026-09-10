#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE="$ROOT/ietf/draft-sankarshan-agent-registry-protocol.md"
HARDENING="$ROOT/ietf/fragments/adversarial-hardening.md"
OUT="$ROOT/ietf/generated"
BASE="draft-sankarshan-agent-registry-protocol-00"
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
if [ ! -f "$HARDENING" ]; then
  echo "error: missing IETF hardening fragment: $HARDENING" >&2
  exit 2
fi

python3 - "$SOURCE" "$HARDENING" "$COMBINED" <<'PY'
from pathlib import Path
import sys
source = Path(sys.argv[1]).read_text(encoding="utf-8")
fragment = Path(sys.argv[2]).read_text(encoding="utf-8").strip()
unnumbered = "\n# Acknowledgements\n{:unnumbered}\n"
numbered = "\n# Acknowledgements\n"
if unnumbered in source:
    combined = source.replace(
        unnumbered,
        f"\n\n{fragment}\n\n# Acknowledgements\n{{:unnumbered}}\n",
        1,
    )
elif numbered in source:
    # The source may intentionally omit kramdown's unnumbered attribute.
    # Preserve that source form while inserting the generated hardening
    # fragment immediately before Acknowledgements.
    combined = source.replace(
        numbered,
        f"\n\n{fragment}\n\n# Acknowledgements\n",
        1,
    )
else:
    raise SystemExit("error: IETF source is missing the Acknowledgements marker")
Path(sys.argv[3]).write_text(combined, encoding="utf-8")
PY

kramdown-rfc "$COMBINED" > "$OUT/$BASE.xml"
xml2rfc --text --out "$OUT/$BASE.txt" "$OUT/$BASE.xml"
xml2rfc --html --out "$OUT/$BASE.html" "$OUT/$BASE.xml"

echo "Built from:"
echo "  ietf/draft-sankarshan-agent-registry-protocol.md"
echo "  ietf/fragments/adversarial-hardening.md"
echo "Built:"
echo "  ietf/generated/$BASE.xml"
echo "  ietf/generated/$BASE.txt"
echo "  ietf/generated/$BASE.html"
