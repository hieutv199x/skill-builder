---
name: de-review-code
description: >-
  Review code changes for correctness, security, compatibility, tests, and
  maintainability using enterprise guardrails. Use for PR/diff review. Do not
  implement features unless the user also asks for fixes.
metadata:
  version: "1.1.0"
  owner: "platform-engineering"
  category: "workflow"
---

# Review Code

## Scope

**Allowed:** structured findings with severity; suggested fixes only when asked.

**Excluded:** drive-by rewrites; rubber-stamp without reading the diff.

## Workflow

1. Detect stack; open matching framework/language skills mentally for expectations
2. Correctness vs requirements/contracts
3. Apply de-secure-coding + de-coding-quality checklists
4. Tests adequacy + version compatibility assumptions
5. Report by severity with paths ([references/checklist.md](references/checklist.md))

## Severity

- **Critical** — security, data loss, auth break, accidental contract break
- **Major** — incorrect behavior, missing critical tests
- **Minor** — maintainability gaps
- **Nit** — optional style already enforced by tools

## References

- [references/checklist.md](references/checklist.md)
- [references/severity.md](references/severity.md)

## Output Contract

Findings by severity; residual risks; testing gaps; verdict.
