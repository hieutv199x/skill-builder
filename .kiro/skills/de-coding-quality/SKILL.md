---
name: de-coding-quality
description: >-
  Enforce maintainable code quality during implementation and review: naming,
  structure, complexity, duplication, error handling, readability, and adherence
  to the repository's formatter/linter. Use when improving quality, reviewing
  diffs for maintainability, or as a companion to framework skills. Do not use
  as a substitute for framework-development skills or for large unrelated cleanups.
metadata:
  version: "1.1.0"
  owner: "platform-engineering"
  category: "foundation"
---

# Coding Quality

## Scope

**Allowed:** quality guidance and small refactors inside the active change set; lint/format fixes required for the task.

**Excluded:** repo-wide cleanups; framework selection; security deep-dives (`de-secure-coding`); inventing style that fights the repo.

## Detect

1. Formatter/linter config (prettier, eslint, spotless, ruff, editorconfig, etc.)
2. `AGENTS.md` style MUST/SHOULD
3. Neighboring code style — match it

## Workflow

1. Read project style evidence before judging
2. Prefer automated tools over subjective nits
3. Limit comments to non-obvious why
4. Remove dead code **introduced by this change**
5. Run lint/format/typecheck; record results

## Decision rules

1. Repo tooling > personal preference
2. Incremental diffs > opportunistic rewrites
3. If quality fix expands scope materially, ask or split

## Guardrails

- No drive-by refactors outside the task
- No disabling lint rules to land features
- No fabricated lint success

## References

- [references/checklist.md](references/checklist.md)
- [references/smells.md](references/smells.md)

## Output Contract

Findings; quality-related files; lint/format evidence.
