---
name: de-testing-strategy
description: >-
  Plan and implement appropriate tests (unit, integration, contract, e2e) using
  the repository's real test stack and commands. Use when deciding coverage,
  writing tests for a change, or verifying behavior. Never claim tests passed
  without executing them and capturing exit codes.
metadata:
  version: "1.1.0"
  owner: "platform-engineering"
  category: "foundation"
---

# Testing Strategy

## Scope

**Allowed:** choose test levels, write/update tests, run targeted verification, document gaps.

**Excluded:** inventing a new test framework without need; fabricating PASS; deleting failing tests to greenwash.

## Detect

1. Test frameworks and folder layout
2. CI test jobs/commands
3. Existing fixtures/factories/fakes
4. Contract/e2e harness presence

## Workflow

1. Assess risk of the change
2. Pick lowest level that gives confidence ([references/test-levels.md](references/test-levels.md))
3. Cover happy path + validation failure + authz denial when relevant
4. Run targeted tests; broaden if integration risk high
5. Record commands, exit codes, skipped checks + why

## Decision rules

| Risk | Prefer |
|---|---|
| Pure logic | Unit |
| DB/API wiring | Integration / Testcontainers analogue |
| Public HTTP contract | Contract/API tests |
| Critical journey | Narrow e2e if harness exists |

## Guardrails

- Match assertion/structure style
- Don’t skip failing tests to hide defects
- Evidence required for PASS claims

## References

- [references/test-levels.md](references/test-levels.md)
- [references/authoring.md](references/authoring.md)

## Output Contract

Tests added/updated; commands/results; remaining gaps.
