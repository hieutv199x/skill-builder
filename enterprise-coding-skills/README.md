# Enterprise Coding Skills

Independent, reusable AI coding skills — **one skill = one capability** — for multi-language and multi-framework development.

Compatible with the [Agent Skills Open Specification](https://agentskills.io/specification). Sync individual skill folders into `.kiro/skills/` or `.cursor/skills/` as needed.

## Principle

Each skill stands alone. Enable only the skill(s) relevant to the current task. Do not load unrelated framework or language skills.

## Categories

| Category | Purpose |
|---|---|
| `foundation` | Cross-cutting analysis, quality, security, testing |
| `language-development` | Language idioms (not framework features) |
| `framework-development` | Framework feature implementation |
| `workflow` | Task orchestration (feature, defect, refactor, review, AGENTS.md) |

## Skills catalog

### Foundation
- `de-repository-analyzer`
- `de-coding-quality`
- `de-secure-coding`
- `de-testing-strategy`

### Language development
- `de-java-development`
- `de-typescript-development`
- `de-python-development`
- `de-csharp-development`
- `de-kotlin-development`
- `de-swift-development`

### Framework development
- `de-spring-boot-development`
- `de-angular-development`
- `de-react-development`
- `de-fastapi-development`
- `de-django-development`
- `de-nestjs-development`
- `de-aspnet-core-development`
- `de-android-development`
- `de-swiftui-development`
- `de-go-development`
- `de-flutter-development`
- `de-backbase-service-development`
- `de-backbase-angular-development`

### Workflows
- `de-repository-audit-agents` — deep audit → generate standards-compliant `AGENTS.md`
- `de-backfill-agents-md` — backfill/refresh `AGENTS.md` workflow (merge, rollout, review)
- `de-implement-feature`
- `de-fix-defect`
- `de-refactor-service`
- `de-review-code`

## Registry

- `registry/catalog.yaml` — index of independent skills
- `registry/compatibility.yaml` — version guidance per framework skill

## Validate

```bash
python3 tooling/validate-catalog.py
```

## Layout

Each skill is a **separate folder** with its own `SKILL.md`, optional `references/`, `scripts/`, and `evals/`.

See `../enterprise-ai-coding-skills-guide.md` for design principles and release gates.
