# Enterprise Coding Skills (Kiro)

Reusable, **independent** Agent Skills for multi-language / multi-framework development. Optimized for **Kiro IDE / Kiro CLI** via `.kiro/skills/`, also usable from Cursor by copying selected skills into `.cursor/skills/`.

## Layout

```text
.kiro/skills/                 # real skill directories for Kiro (copied, not symlinks)
enterprise-coding-skills/     # editable source of truth
  foundation/
  languages/
  frameworks/
  workflows/
  registry/
  templates/
  tooling/
enterprise-ai-coding-skills-guide.md
```

Kiro discovers skills under `.kiro/skills/<skill-name>/SKILL.md`.  
Edit skills under `enterprise-coding-skills/`, then sync into `.kiro/skills/`.

## Setup (this repo)

```bash
# copy skills into real .kiro/skills/<name>/ directories after editing source
python3 tooling/sync-kiro-skills.py

# validate catalog + SKILL.md presence
python3 enterprise-coding-skills/tooling/validate-catalog.py
```

## Use in another project

**Copy selected skills** (directory name must match frontmatter `name`):

```bash
mkdir -p /path/to/app/.kiro/skills
cp -R .kiro/skills/de-spring-boot-development /path/to/app/.kiro/skills/
cp -R .kiro/skills/de-repository-audit-agents /path/to/app/.kiro/skills/
```

Or copy from source:

```bash
cp -R enterprise-coding-skills/frameworks/spring-boot \
  /path/to/app/.kiro/skills/de-spring-boot-development
```

**Global Kiro skills**

```bash
mkdir -p ~/.kiro/skills
cp -R .kiro/skills/de-spring-boot-development ~/.kiro/skills/
```

In Kiro, invoke by name (e.g. `/de-repository-audit-agents`) or rely on description-based discovery.

## Suggested starters

| Goal | Skill |
|---|---|
| Detect stack | `de-repository-analyzer` |
| Deep audit → `AGENTS.md` | `de-repository-audit-agents` |
| Backfill / refresh `AGENTS.md` | `de-backfill-agents-md` |
| Spring feature work | `de-spring-boot-development` |
| Angular feature work | `de-angular-development` |
| Backbase backend | `de-backbase-service-development` |
| Backbase Angular | `de-backbase-angular-development` |

Enable **only** the independent skills needed for the task.

## Validate

```bash
python3 enterprise-coding-skills/tooling/validate-catalog.py
python3 tooling/sync-kiro-skills.py
find .kiro/skills -type l   # should print nothing
```

## Notes

- One skill = one capability.
- Skill names use the `de-*` prefix.
- `AGENTS.md` is per-service policy; skills are reusable knowledge.
- Backbase skills are enterprise-proposed process/guardrails — they do not invent proprietary SDK APIs.
- See `enterprise-ai-coding-skills-guide.md` for design principles.
