---
name: de-csharp-development
description: >-
  Write and modify idiomatic C# code with version-aware language features,
  packaging/modules, error handling, and the repository's test/lint toolchain.
  Use for C# language-level work. Prefer de-aspnet-core-development when those frameworks
  are the primary task focus — this skill complements them, it does not replace them.
metadata:
  version: "1.1.0"
  owner: "platform-engineering"
  category: "language-development"
  language: "csharp"
---

# C# Development

## Scope

**Allowed:** idiomatic C#, shared libraries, language-level refactors, unit tests, lint/type fixes.

**Excluded:** Replacing the matching framework skill for feature delivery; inventing unsupported language features for the detected toolchain version.

## Detect

1. Toolchain from *.csproj / global.json
2. Language level / compiler options / strictness flags
3. Formatter/linter/test runner already configured
4. Package/module layout conventions
5. `AGENTS.md` / steering

Read [references/conventions.md](references/conventions.md) and [references/tooling.md](references/tooling.md).

## Preconditions

- [ ] Language/toolchain version recorded
- [ ] Test & lint commands evidenced
- [ ] Public API surface impact assessed for library changes

## Workflow

1. Analyze call sites and existing idioms in neighboring code
2. Plan minimal file set — no drive-by style rewrites
3. Implement using version-supported features only
4. Run targeted tests + lint/typecheck
5. Report evidence

## Decision rules

1. Installed language level > “modern best practice” blogs
2. Framework skill owns framework features; this skill owns idioms/types/modules
3. Don’t weaken strictness flags to land a change
4. Match error-handling style already used in the module

## Guardrails

- No secrets in samples/tests
- No fabricated verification
- No unrelated refactors

## References

- [references/conventions.md](references/conventions.md)
- [references/tooling.md](references/tooling.md)
- [references/anti-patterns.md](references/anti-patterns.md)

## Output Contract

Toolchain versions; files; commands/exit codes; risks.
