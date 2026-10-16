# ChatGPT Skills — Official Documentation Index

## Status
- **Status:** Reference / documentation index.
- **Purpose:** Collect official OpenAI references for understanding, authoring, and managing Skills.
- **Last reviewed:** 2026-10-16.
- **Important:** Skills in ChatGPT, Agent Skills using `SKILL.md`, and the Skills API are related but distinct interfaces. Do not assume a file committed to GitHub is automatically installed in ChatGPT.

## Official references

### 1. Skills in ChatGPT
- **URL:** https://help.openai.com/en/articles/20001066-skills-in-chatgpt
- **Use for:** ChatGPT product-level guidance about creating, importing/uploading, using, sharing, or managing skills in the ChatGPT interface.
- **Verification note:** Availability may depend on plan, workspace settings, rollout, and current product behavior. Check the article and the user's own interface before making a definitive availability claim.

### 2. Skills developer guide
- **URL:** https://developers.openai.com/api/docs/guides/tools-skills
- **Use for:** Technical guidance about Skills, including reusable instructions and the skill file structure.
- **Use when:** Designing or reviewing a skill directory and its `SKILL.md` instructions.

### 3. Skills API reference
- **URL:** https://developers.openai.com/api/reference/resources/skills
- **Use for:** API-level operations and schemas for managing Skills programmatically.
- **Caution:** API support and product UI support are not interchangeable. Follow the documented API contract for any programmatic integration.

### 4. Official Skill Creator source
- **URL:** https://github.com/openai/skills/blob/main/skills/.system/skill-creator/SKILL.md
- **Use for:** An official example/reference for creating and improving skills.
- **Caution:** Treat repository content as versioned source code. Recheck the current file before relying on implementation details.

### 5. Connected apps in ChatGPT
- **URL:** https://help.openai.com/en/articles/11487775-connected-apps-in-chatgpt
- **Use for:** Documentation about connecting apps to ChatGPT, app permissions, and connected-app behavior.
- **Relationship:** This is relevant when a skill explains workflows involving connected apps, but it is not itself a Skills authoring specification.

## Recommended review workflow

1. Start with **Skills in ChatGPT** to understand the product interface and availability.
2. Read the **Skills developer guide** for the expected technical structure and authoring conventions.
3. Consult the **Skills API reference** only when the task specifically involves programmatic API management.
4. Review the **official Skill Creator source** for a concrete authoring reference.
5. Use the **Connected apps** article when the skill's scope involves external app connections, permissions, or data sharing.
6. Verify each relevant source before implementing changes; distinguish confirmed documentation from assumptions.
7. After drafting a skill, review its scope, trigger conditions, instructions, references, and safety boundaries before treating it as ready to use.

## Repository conventions

- Store skill-related reference material under `skill/`.
- Keep draft instructions clearly labeled as drafts until reviewed.
- Do not claim a skill is installed, enabled, published, or available in ChatGPT solely because its Markdown file exists in this repository.
- Prefer official OpenAI documentation as the source of truth; record the URL and review date for future maintenance.
- When product behavior may have changed, re-open the official source instead of relying on this index alone.

## Maintenance checklist

- [ ] Check that each official URL still resolves and points to the intended documentation.
- [ ] Review product availability and plan/workspace caveats.
- [ ] Confirm whether technical file-format requirements have changed.
- [ ] Update the review date after checking the sources.
- [ ] Keep this index descriptive; do not copy large portions of source documentation.
