---
name: de-refactor-service
description: >-
  Refactor a service or module safely while preserving behavior, keeping diffs
  focused, and using tests as a safety net. Use for intentional refactors. Do
  not mix large refactors with features/bugfixes when avoidable; do not silently
  change public contracts.
metadata:
  version: "1.1.0"
  owner: "platform-engineering"
  category: "workflow"
---

# Refactor Service

## Scope

**Allowed:** behavior-preserving structural improvements within agreed scope.

**Excluded:** silent behavior changes; dependency major upgrades disguised as refactors; spreading BAD legacy patterns.

## Workflow

1. Define goal/non-goals; identify characterization tests
2. Add characterization coverage if missing and feasible
3. Incremental refactors (extract/rename/move) via language/framework skills
4. Test after meaningful steps
5. Report before/after + evidence ([references/safety.md](references/safety.md))

## Guardrails

- Vertical slices > whole-service rewrites
- Separate upgrade PRs
- BAD patterns stay labeled BAD

## References

- [references/safety.md](references/safety.md)

## Output Contract

Scope; steps; tests; behavior-preservation evidence; follow-ups.
