# Enterprise Coding Skills (Kiro)

Reusable, **independent** Agent Skills for multi-language / multi-framework development. Optimized for **Kiro IDE / Kiro CLI** via `.kiro/skills/`, also usable from Cursor by syncing selected skills into `.cursor/skills/`.

## Layout

```text
.kiro/skills/                 # flat skill entries for Kiro (symlinks)
enterprise-coding-skills/     # source of truth
  foundation/
  languages/
  frameworks/
  workflows/
  registry/
  templates/
  tooling/
enterprise-ai-coding-skills-guide.md
```

Kiro discovers skills under `.kiro/skills/<skill-name>/SKILL.md`. Each entry is a symlink to the corresponding folder under `enterprise-coding-skills/`.

## Setup (this repo)

```bash
# regenerate .kiro/skills symlinks after adding a skill
python3 tooling/sync-kiro-skills.py

# validate catalog + SKILL.md presence
python3 enterprise-coding-skills/tooling/validate-catalog.py
```

## Use in another project

**Option A — copy selected skills**

```bash
mkdir -p /path/to/app/.kiro/skills
cp -R enterprise-coding-skills/frameworks/spring-boot \
  /path/to/app/.kiro/skills/spring-boot-development
```

(Use the skill folder that contains `SKILL.md`; the directory name should match the skill `name` in frontmatter.)

**Option B — symlink from this repo**

```bash
ln -s /absolute/path/to/Skill-builder/.kiro/skills/spring-boot-development \
  /path/to/app/.kiro/skills/spring-boot-development
```

**Option C — global Kiro skills**

```bash
mkdir -p ~/.kiro/skills
# link or copy the skills you need into ~/.kiro/skills/
```

In Kiro, invoke by name (e.g. `/repository-audit-agents`) or rely on description-based discovery.

## Suggested starters

| Goal | Skill |
|---|---|
| Detect stack | `repository-analyzer` |
| Deep audit → `AGENTS.md` | `repository-audit-agents` |
| Backfill / refresh `AGENTS.md` | `backfill-agents-md` |
| Spring feature work | `spring-boot-development` |
| Angular feature work | `angular-development` |
| Backbase backend | `backbase-service-development` |
| Backbase Angular | `backbase-angular-development` |

Enable **only** the independent skills needed for the task.

## Validate

```bash
python3 enterprise-coding-skills/tooling/validate-catalog.py
ls -la .kiro/skills | head
```

## Notes

- One skill = one capability.
- `AGENTS.md` is per-service policy; skills are reusable knowledge.
- Backbase skills are enterprise-proposed process/guardrails — they do not invent proprietary SDK APIs.
- See `enterprise-ai-coding-skills-guide.md` for design principles.
