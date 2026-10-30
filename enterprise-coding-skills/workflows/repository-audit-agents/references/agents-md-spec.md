# AGENTS.md — Canonical Spec

`AGENTS.md` is **short, service-specific policy** for agents working in this repository. It is not a tutorial and not a dump of enterprise framework skills.

Canonical skeleton (also in `templates/AGENTS.md.template`):

```markdown
# Service Development Instructions

## Identity
- Service: [name]
- Stack: [detected versions]
- Build/test tools: [actual commands]

## Architecture
- Responsibilities and boundaries: [verified]
- Entry points: [paths]
- Contracts and dependencies: [paths]

## Coding Rules
- MUST: [rules evidenced by project/reference standards]
- SHOULD: [preferred conventions]
- MUST NOT: [verified anti-patterns + reason]

## Workflow
- Read relevant contracts before editing.
- Use applicable enterprise skills.
- Run targeted checks before declaring completion.

## Known Exceptions / Legacy Debt
- [file/pattern, rationale, remediation scope]

## Evidence
- [repo paths, build outputs, approved architectural sources]
```

## Section rules

### Identity
- Real service/module name as used by the team
- Versions from manifests/lockfiles with confidence if not exact
- Commands copied from `package.json` scripts, Maven/Gradle wrappers, Makefile, or CI — **verbatim where possible**

### Architecture
- What this service owns vs calls
- Concrete paths: `src/main/java/.../api`, `apps/web/src/app`, etc.
- Contract locations: `openapi.yaml`, `libs/api-client`, etc.
- Avoid aspirational architecture that the code does not reflect

### Coding Rules
- **MUST** — non-negotiable for agents (safety, contracts, auth, generated-code policy)
- **SHOULD** — preferred when multiple valid options exist
- **MUST NOT** — always include **why** (security, breakage, observed incident class)
- Each bullet should be testable against a future change
- Prefer ≤ 7 MUST, ≤ 7 SHOULD, ≤ 7 MUST NOT unless the service is unusually complex — length kills compliance

### Workflow
- 3–6 bullets max
- Point to contracts, tests, and which independent skills apply by name
- Require real verification before “done”

### Known Exceptions / Legacy Debt
- Pattern + path/glob + why accepted + whether agents may extend it
- Default: **do not spread** legacy; only touch when the task requires it

### Evidence
- Paths and CI job names that justify the rules
- Date or commit/sha optional but useful for refresh triggers

## File placement

| Context | Prefer |
|---|---|
| Single service repo | `/AGENTS.md` |
| Monorepo | `/services/<name>/AGENTS.md` or package root that agents will open |
| Experience + API | Separate AGENTS.md per deployable — don’t merge conflicting stacks |

## Naming

Prefer `AGENTS.md`. If the estate already standardized another name, follow the estate and note it in Evidence — do not create duplicates that drift.
