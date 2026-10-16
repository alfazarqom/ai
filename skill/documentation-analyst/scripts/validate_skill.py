#!/usr/bin/env python3
"""Basic structure checks for this skill package. Uses Python standard library only."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
skill_file = root / "SKILL.md"
errors = []

if not skill_file.is_file():
    errors.append("SKILL.md is missing.")
else:
    body = skill_file.read_text(encoding="utf-8")
    if not body.startswith("---\n"):
        errors.append("SKILL.md must begin with YAML frontmatter.")
    else:
        parts = body.split("---", 2)
        if len(parts) < 3:
            errors.append("YAML frontmatter is not closed.")
        else:
            frontmatter = parts[1]
            for field in ("name", "description"):
                if not re.search(r"(?m)^" + field + r":\s*\S.+$", frontmatter):
                    errors.append("Missing non-empty frontmatter field: " + field)

    if "{{" in body or "}}" in body:
        errors.append("Unresolved template placeholder found in SKILL.md.")

required = [
    "agents/openai.yaml",
    "references/official-sources.md",
    "references/workflow-guide.md",
    "assets/report-template.md",
]
for relative in required:
    if not (root / relative).is_file():
        errors.append("Required package file is missing: " + relative)

if errors:
    for error in errors:
        print("ERROR:", error)
    sys.exit(1)

print("PASS: SKILL.md frontmatter and required package files are present.")
