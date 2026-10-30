---
name: de-implement-feature
description: >-
  End-to-end workflow to implement a product feature safely: analyze repository,
  select language/framework skills, plan, implement minimally, verify with
  evidence, and report. Use for user stories/features. Do not use for AGENTS.md
  backfill-only or pure review-only tasks.
metadata:
  version: "1.1.0"
  owner: "platform-engineering"
  category: "workflow"
---

# Implement Feature

## Scope

**Allowed:** orchestrate analyze → implement → verify for a feature.

**Excluded:** unapproved public contract breaks; auto-merge/deploy; loading unrelated stacks.

## Workflow

1. Run/apply `de-repository-analyzer`; read AGENTS.md/contracts
2. Select **one** primary framework skill (+ language skill if needed) — see [references/skill-selection.md](references/skill-selection.md)
3. Plan impacted files/tests; list assumptions
4. Implement minimal change using those skills’ guardrails
5. Apply `de-testing-strategy`; add `de-secure-coding` / `de-coding-quality` only when relevant
6. Verify with real commands; report Output Contract

## Skill selection rules

- Enable independent skills only — never load unrelated frameworks
- Typical: this workflow + one framework skill (+ language if needed)
- Backbase work: Backbase skill; add Spring/Angular skill only if the change needs that base guidance

## Guardrails

- Incremental diffs
- No fabricated verification
- State assumptions when evidence missing

## References

- [references/skill-selection.md](references/skill-selection.md)
- [references/report-template.md](references/report-template.md)

## Output Contract

Plan; skills used; files; verification evidence; risks/approvals.
