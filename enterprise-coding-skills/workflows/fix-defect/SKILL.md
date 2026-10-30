---
name: de-fix-defect
description: >-
  Diagnose and fix bugs with evidence: reproduce, locate root cause, apply a
  minimal fix, add regression tests, and verify. Use for defect/bug tasks. Do
  not use for net-new features or broad refactors disguised as fixes.
metadata:
  version: "1.1.0"
  owner: "platform-engineering"
  category: "workflow"
---

# Fix Defect

## Scope

**Allowed:** focused bug fixes with regression coverage.

**Excluded:** opportunistic refactors; feature expansions; silencing failures.

## Workflow

1. Gather evidence (log, failing test, repro)
2. Detect stack; open the matching framework skill
3. Hypothesize root cause; prove before large edits ([references/diagnosis.md](references/diagnosis.md))
4. Minimal fix
5. Regression test that fails without the fix when feasible
6. Targeted verification + report

## Guardrails

- Don’t catch-and-ignore as a “fix”
- Don’t delete/skip tests to greenwash
- Prefer root cause over symptom-only when safe/in scope

## References

- [references/diagnosis.md](references/diagnosis.md)
- [references/report-template.md](references/report-template.md)

## Output Contract

Root cause; fix; regression test; verification evidence.
