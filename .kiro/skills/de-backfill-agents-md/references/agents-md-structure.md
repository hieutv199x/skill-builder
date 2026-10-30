# AGENTS.md Structure (backfill)

Use this skeleton (same as `templates/AGENTS.md.template`):

```markdown
# Service Development Instructions

## Identity
- Service: [name]
- Stack: [versions from manifests/lockfiles]
- Build/test tools: [exact commands from scripts/CI]

## Architecture
- Responsibilities and boundaries: [...]
- Entry points: [paths]
- Contracts and dependencies: [paths]

## Coding Rules
- MUST: [...]
- SHOULD: [...]
- MUST NOT: [... — include reason]

## Workflow
- Read contracts before editing.
- Prefer independent skills: [names]
- Run targeted checks; record real results.

## Known Exceptions / Legacy Debt
- [path/pattern]: [why] — do not spread unless task requires it.

## Evidence
- [paths / CI]
- Last audited: [YYYY-MM-DD]
```

## Field quality

| Section | Must be |
|---|---|
| Identity | Factual versions + runnable commands |
| Architecture | Real paths, not aspirational diagrams |
| Coding Rules | Enforceable; ≤7 bullets per MUST/SHOULD/MUST NOT when possible |
| Workflow | 3–6 steps max |
| Legacy | Explicit non-spread default |
| Evidence | Traceable |

`AGENTS.md` ≠ framework textbook. Keep service-specific policy only.
