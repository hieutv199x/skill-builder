---
name: de-backfill-agents-md
description: >-
  Backfill or refresh evidence-based AGENTS.md for a service or monorepo package:
  inventory stack, classify patterns (GOOD / LEGACY-ACCEPTED / BAD / UNKNOWN),
  draft MUST/SHOULD/MUST NOT rules, merge safely with existing guidance, and
  prepare owner review. Use when onboarding repos, rolling out AGENTS.md, or
  refreshing stale instructions. Do not use for product feature implementation.
  Never promote common bad patterns into MUST/SHOULD.
metadata:
  version: "1.3.0"
  owner: "platform-engineering"
  category: "workflow"
---

# Backfill AGENTS.md

Independent workflow to **produce or refresh** a standards-compliant `AGENTS.md` from repository evidence.

Related skill: `de-repository-audit-agents` (deeper audit rubric / inventory scripts). This skill owns the **backfill delivery workflow** (draft → merge → review → handoff). Either skill may be used alone; together they reinforce quality.

## Scope

**Allowed**
- Single-service or single-package `AGENTS.md` backfill
- Safe refresh when `AGENTS.md` already exists (preserve intentional owner rules)
- Pattern sampling + classification → Coding Rules
- Draft audit notes / owner questions
- Recommend independent enterprise skills for the Workflow section

**Excluded**
- Implementing product features or refactors
- Silent overwrite of owner-approved rules without calling out diffs
- Auto-merge / skip review
- Dumping entire framework skill manuals into `AGENTS.md`
- Inventing build commands, versions, or vendor SDK APIs

## Detect

| Input | Evidence |
|---|---|
| Target path | Repo root vs `services/x` / `apps/y` (confirm with user if ambiguous) |
| Existing guidance | `AGENTS.md`, `.cursor/rules`, `.kiro/steering`, CONTRIBUTING |
| Stack/versions | Manifests + lockfiles |
| Commands | `package.json` scripts, Maven/Gradle wrappers, Makefile, CI |
| Contracts | OpenAPI / proto / generated clients |
| Samples | 1–3 representative features with tests when possible |

Optional: run `../de-repository-audit-agents/scripts/inventory.py` or `de-repository-analyzer` `detect-stack.py` when available.

## Preconditions

- [ ] Target `AGENTS.md` path agreed
- [ ] Working tree understood (`git status`) — do not discard user changes
- [ ] If file exists: read it fully before drafting
- [ ] Stack confidence recorded (high/medium/low)

## Workflow

### 1. Protect existing work
- Inspect git status; never wipe local edits
- If `AGENTS.md` exists: extract intentional MUST/SHOULD/MUST NOT; mark which to keep, revise, or drop with reason ([references/merge-existing.md](references/merge-existing.md))

### 2. Inventory
- Versions, modules, entry points, contracts, CI commands
- Fill Identity fields with evidenced commands only
- See [references/backfill-playbook.md](references/backfill-playbook.md)

### 3. Sample & classify
- 1–3 features; label `GOOD` / `LEGACY-ACCEPTED` / `BAD` / `UNKNOWN`
- [references/pattern-classification.md](references/pattern-classification.md)
- Do **not** promote BAD → SHOULD because it is common

### 4. Draft AGENTS.md
- Structure: [references/agents-md-structure.md](references/agents-md-structure.md) (aligned with `templates/AGENTS.md.template`)
- Writing style: [references/writing-rules.md](references/writing-rules.md)
- Map classifications → MUST / SHOULD / MUST NOT / Legacy
- Keep short (~80–180 lines); link paths

### 5. Self-check
- [references/quality-checklist.md](references/quality-checklist.md)
- Mentally test rules on “add a field” and “fix a null bug”

### 6. Handoff
- Present draft + diff vs previous (if any) + open questions
- Label **draft pending owner review**
- Do not treat as authoritative until approved
- Schedule re-backfill triggers ([references/refresh-policy.md](references/refresh-policy.md))

## Decision rules

1. Security/legal > approved contracts > version compatibility > AGENTS owner intent > evidenced GOOD patterns > framework defaults > weak examples  
2. Common ≠ good  
3. Missing evidence → UNKNOWN / question — never fabricate  
4. Monorepo: one AGENTS.md per deployable stack when rules would conflict  
5. Prefer additive refreshes; call out removals of old rules explicitly  

## Guardrails

- No secrets in AGENTS.md  
- No invented npm/Maven scripts  
- No unverified Backbase/vendor APIs  
- No auto-merge  
- No application code changes under the guise of backfill  

## References

| When | Read |
|---|---|
| End-to-end steps | [references/backfill-playbook.md](references/backfill-playbook.md) |
| File structure | [references/agents-md-structure.md](references/agents-md-structure.md) |
| Pattern labels | [references/pattern-classification.md](references/pattern-classification.md) |
| MUST/SHOULD writing | [references/writing-rules.md](references/writing-rules.md) |
| Existing file merge | [references/merge-existing.md](references/merge-existing.md) |
| Quality checklist | [references/quality-checklist.md](references/quality-checklist.md) |
| When to re-run | [references/refresh-policy.md](references/refresh-policy.md) |
| Examples | [references/examples.md](references/examples.md) |
| Skill name hints | [references/skill-hints.md](references/skill-hints.md) |

## Output Contract

```markdown
## Backfill result
- AGENTS.md path (draft):
- Created | Updated (diff summary):
- Stack + confidence:
- Commands evidenced:
- Classification counts (GOOD/BAD/LEGACY/UNKNOWN):
- Rules kept from previous AGENTS.md:
- Rules added/removed:
- Open questions for owner:
- Recommended independent skills:
- Review status: draft | awaiting owner
```
