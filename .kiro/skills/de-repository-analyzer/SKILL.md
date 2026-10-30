---
name: de-repository-analyzer
description: >-
  Detect a repository tech stack, language/framework versions, build and test
  tools, entry points, contracts, and project guidance (AGENTS.md / steering).
  Use before implementing features, generating AGENTS.md, or selecting framework
  skills. Do not use for writing application features or changing production
  behavior unless asked only to write an analysis report.
metadata:
  version: "1.1.0"
  owner: "platform-engineering"
  category: "foundation"
---

# Repository Analyzer

## Scope

**Allowed:** inventory manifests, versions, layouts, test/build commands, contracts, guidance files; report confidence and gaps; recommend applicable independent skills.

**Excluded:** implementing features; refactoring; dependency upgrades; inventing undocumented APIs.

## Detect

1. Build manifests/lockfiles ([references/detection-signals.md](references/detection-signals.md))
2. Exact versions from manifests/lockfiles
3. Layout: monorepo vs single service; source/test roots
4. Contracts: OpenAPI/AsyncAPI/proto/GraphQL + generation config
5. Guidance: AGENTS.md, `.kiro/steering/`, `.cursor/rules/`, CONTRIBUTING, architecture docs
6. Optionally run `scripts/detect-stack.py` for a deterministic dump

## Workflow

1. Scan root + one level of packages/modules
2. Map signals → candidate stacks with confidence (`high`/`medium`/`low`)
3. Note conflicts and unresolved versions
4. Recommend applicable independent skills — exclude unrelated stacks
5. Report via [references/report-template.md](references/report-template.md)

## Guardrails

- Never invent versions
- Label observed patterns as observed — not automatic standards
- Don’t modify files unless asked for a written report artifact

## References

- [references/detection-signals.md](references/detection-signals.md)
- [references/report-template.md](references/report-template.md)
- [references/skill-mapping.md](references/skill-mapping.md)

## Output Contract

Stacks+confidence; commands; contracts; guidance; recommended skills; gaps.
