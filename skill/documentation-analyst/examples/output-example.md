# Example output shape

## Summary
The skill package requires a `SKILL.md` containing YAML frontmatter with `name` and `description`, plus instructions in Markdown.

## Required
- `SKILL.md`
- Non-empty `name` and `description` fields in frontmatter

## Optional supporting resources
- `references/` for supporting documentation
- `scripts/` for repeatable deterministic tasks
- `assets/` for files used in generated output
- `agents/openai.yaml` for supported UI-facing metadata

## Caveats
Optional files should be added only when they directly support the skill's workflow.

## Sources
- https://developers.openai.com/api/docs/guides/tools-skills
- https://github.com/openai/skills/blob/main/skills/.system/skill-creator/SKILL.md
