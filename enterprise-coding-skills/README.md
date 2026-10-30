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
- `repository-analyzer`
- `coding-quality`
- `secure-coding`
- `testing-strategy`

### Language development
- `java-development`
- `typescript-development`
- `python-development`
- `csharp-development`
- `kotlin-development`
- `swift-development`

### Framework development
- `spring-boot-development`
- `angular-development`
- `react-development`
- `fastapi-development`
- `django-development`
- `nestjs-development`
- `aspnet-core-development`
- `android-development`
- `swiftui-development`
- `go-development`
- `flutter-development`
- `backbase-service-development`
- `backbase-angular-development`

### Workflows
- `repository-audit-agents` — deep audit → generate standards-compliant `AGENTS.md`
- `backfill-agents-md` — backfill/refresh `AGENTS.md` workflow (merge, rollout, review)
- `implement-feature`
- `fix-defect`
- `refactor-service`
- `review-code`

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
