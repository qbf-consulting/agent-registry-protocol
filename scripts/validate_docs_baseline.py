#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
PRIMARY = [
    ROOT / "docs/start-here.md",
    ROOT / "docs/understand.md",
    ROOT / "docs/index.md",
]
PUBLICATION_MAP = ROOT / "docs/publication-map.yml"

errors = []

required_current = {
    "docs/start-here.md": [
        "Candidate Specification v0.10.0",
        "draft-sankarshan-agent-registry-protocol-02",
        "Current implementation release line",
    ],
    "docs/understand.md": [
        "Candidate Specification v0.10.0",
    ],
    "docs/index.md": [
        "Candidate v0.10.0",
        "draft-sankarshan-agent-registry-protocol-02",
    ],
}

for path in PRIMARY:
    text = path.read_text()
    rel = str(path.relative_to(ROOT))
    for token in required_current[rel]:
        if token not in text:
            errors.append(f"{rel}: missing current-baseline token: {token}")

start = (ROOT / "docs/start-here.md").read_text()
understand = (ROOT / "docs/understand.md").read_text()

for rel, text in [("docs/start-here.md", start), ("docs/understand.md", understand)]:
    if "agent-registry-protocol-v0.9.0.md" in text:
        errors.append(f"{rel}: v0.9.0 must not be linked as the current reader baseline")

if "draft-sankarshan-agent-registry-protocol-00" in start:
    errors.append("docs/start-here.md: obsolete IETF -00 framing remains")

for path in ROOT.joinpath("docs").rglob("*.md"):
    text = path.read_text()
    if "github.com/sankarshanmukhopadhyay/agent-registry-protocol" in text:
        errors.append(f"{path.relative_to(ROOT)}: stale personal-repository URL")

pub = PUBLICATION_MAP.read_text()
for required in [
    "RELEASE_NOTES_v0.10.0.md",
    "spec/agent-registry-protocol-v0.10.0.md",
    "spec/agent-registry-protocol-authority-commitment-pp02.md",
    "spec/agent-registry-protocol-wire-contract-pp03.md",
]:
    if required not in pub:
        errors.append(f"docs/publication-map.yml: missing published source {required}")

if errors:
    print("\n".join(errors))
    sys.exit(1)

print("validate_docs_baseline.py: PASS")
