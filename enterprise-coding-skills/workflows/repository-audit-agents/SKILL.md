---
name: repository-audit-agents
description: >-
  Audit a repository with evidence and generate a standards-compliant AGENTS.md
  (Identity, Architecture, Coding Rules MUST/SHOULD/MUST NOT, Workflow, Legacy
  Debt, Evidence). Use when creating or refreshing AGENTS.md, onboarding a repo
  for agents, or auditing project guidance quality. Do not use for implementing
  product features. Never promote common bad patterns into MUST/SHOULD rules.
metadata:
  version: "1.0.0"
  owner: "platform-engineering"
  category: "workflow"
---

# Repository Audit → AGENTS.md

Independent skill: audit the target repository, classify patterns, and produce a short, evidence-based `AGENTS.md` agents can follow.

`AGENTS.md` is **service policy**, not a framework skill dump. Prefer facts from this repo over generic best practices.

## Scope

**Allowed**
- Inventory stack, versions, build/test commands, contracts, entry points
- Sample and classify code patterns (`GOOD` / `LEGACY-ACCEPTED` / `BAD` / `UNKNOWN`)
- Draft or refresh `AGENTS.md` at repo root or package root (monorepo)
- Produce an audit report + owner-review questions
- Recommend which **independent** enterprise skills fit this repo

**Excluded**
- Implementing product features or drive-by refactors
- Auto-merging without owner review
- Embedding secrets, proprietary vendor docs, or unverified SDK APIs
- Turning `AGENTS.md` into a copy of Spring/Angular/Backbase skill manuals

## Detect / Audit inputs

Collect evidence before writing rules:

| Area | Sources |
|---|---|
| Identity | repo name, module names, README |
| Stack/versions | `pom.xml` / Gradle / `package.json` / lockfiles / `*.csproj` / `go.mod` / `pubspec.yaml` |
| Build/test | wrappers, `package.json` scripts, Makefile, CI workflows |
| Architecture | package layout, ADRs, docs, module boundaries |
| Entry points | `Application`, `main.ts`, `Program.cs`, routes, controllers |
| Contracts | OpenAPI, protos, GraphQL, generated clients |
| Guidance already present | existing `AGENTS.md`, `.cursor/rules`, `.kiro/steering`, CONTRIBUTING |
| Quality signals | linters, formatters, test layout |
| Security signals | auth config, secret handling patterns |

Optional helpers (deterministic, no LLM):
- `scripts/inventory.py <repo-root>` — bounded inventory dump
- `foundation/repository-analyzer/scripts/detect-stack.py` — stack signals

Full audit still requires reading code and CI. Also use [references/audit-rubric.md](references/audit-rubric.md) and [references/validation-checklist.md](references/validation-checklist.md).

Read [references/audit-playbook.md](references/audit-playbook.md).

## Preconditions

- [ ] Target path for `AGENTS.md` confirmed (root vs `apps/x` / `services/y`)
- [ ] Scope confirmed (one service vs whole monorepo — prefer one service file)
- [ ] Access to manifests, source samples, and CI/scripts
- [ ] Framework/version notes available if comparing patterns (optional independent framework skill)

## Workflow

### 1. Inventory
- Detect stack + versions with confidence (`high` / `medium` / `low`)
- Record real build/lint/test commands from scripts/CI — never invent
- List entry points, contracts, important modules

### 2. Sample patterns
- Pick 1–3 representative features (recent, tested preferred)
- Trace each through entry → domain/service → persistence/API
- Classify every notable pattern — [references/pattern-classification.md](references/pattern-classification.md)
- Compare to healthy framework norms only as a **lens**, not as automatic policy

### 3. Draft rules
Map classifications → AGENTS sections using [references/agents-md-spec.md](references/agents-md-spec.md) and [references/writing-rules.md](references/writing-rules.md):

| Classification | AGENTS.md destination |
|---|---|
| `GOOD` | MUST or SHOULD (with evidence path) |
| `LEGACY-ACCEPTED` | Known Exceptions / Legacy Debt |
| `BAD` | MUST NOT (+ reason) |
| `UNKNOWN` | omit rule or list under Gaps — do not invent |

Keep the file **short and specific**. Link paths; avoid essays.

### 4. Write AGENTS.md
- Use structure in [references/agents-md-spec.md](references/agents-md-spec.md) (aligned with `templates/AGENTS.md.template`)
- Fill Identity / Architecture / Coding Rules / Workflow / Legacy / Evidence
- Add recommended independent skills for this stack (names only)
- See good/bad examples: [references/examples.md](references/examples.md)

### 5. Quality gate
Run [references/quality-gate.md](references/quality-gate.md) before calling the draft done.

### 6. Handoff
- Request service-owner review
- Do not treat draft as authoritative until reviewed
- Re-audit when dependencies or architecture change materially

## Decision rules

1. Security/legal > approved contracts > version compatibility > evidenced GOOD patterns > framework skill defaults > weak examples  
2. **Common ≠ good** — frequency never promotes BAD → MUST  
3. If framework guidance conflicts with widespread repo practice: document both; put unsafe practice in MUST NOT or Legacy; do not silently copy legacy into SHOULD  
4. Missing evidence → `UNKNOWN` / open question — never fabricate versions or commands  
5. One `AGENTS.md` per deployable service/package when possible in monorepos  

## Guardrails

- Never invent build/test commands
- Never commit or paste secrets into `AGENTS.md`
- Never encode unverified Backbase/vendor SDK details
- Never block all valid work with overly rigid MUST rules — test rules against 1–2 realistic tasks mentally
- Never auto-merge without owner approval

## References

| When | Read |
|---|---|
| Full audit steps | [references/audit-playbook.md](references/audit-playbook.md) |
| AGENTS.md structure & field rules | [references/agents-md-spec.md](references/agents-md-spec.md) |
| How to write MUST/SHOULD/MUST NOT | [references/writing-rules.md](references/writing-rules.md) |
| Pattern labels | [references/pattern-classification.md](references/pattern-classification.md) |
| Evidence standards | [references/evidence-rules.md](references/evidence-rules.md) |
| Good vs bad samples | [references/examples.md](references/examples.md) |
| Done checklist | [references/quality-gate.md](references/quality-gate.md) |
| Rubric / validation | [references/audit-rubric.md](references/audit-rubric.md), [references/validation-checklist.md](references/validation-checklist.md) |
| Stack → skill names | [references/skill-hints.md](references/skill-hints.md) |
| Template asset | [assets/AGENTS.md.template](assets/AGENTS.md.template) |

## Output Contract

Deliver **both**:

1. **`AGENTS.md`** at the agreed path (draft)
2. **Audit report**

```markdown
## Repository audit report
- Target AGENTS.md path:
- Stack + versions + confidence:
- Build / test / lint commands (evidenced):
- Pattern sample (path → label → note):
- Rules derived (counts MUST / SHOULD / MUST NOT / Legacy):
- Open questions for owner:
- Recommended independent skills:
- Risks / gaps:
```
