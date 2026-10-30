---
name: de-swiftui-development
description: >-
  Implement and modify SwiftUI features: views, navigation, state (Observation/
  ObservableObject/TCA as used), and tests/previews. Use for SwiftUI app work.
  Do not use for Android or backend-only tasks. Do not force APIs newer than the
  deployment target.
metadata:
  version: "1.1.0"
  owner: "platform-engineering"
  category: "framework-development"
  framework: "swiftui"
---

# SwiftUI Development

## Scope

**Allowed:** SwiftUI views, navigation, view models/state stores as patterned, previews, unit/UI tests if present.

**Excluded:** Android; full UIKit rewrites; signing/cert changes.

## Detect

1. Swift tools version; deployment target; platforms
2. SwiftUI vs UIKit mix in the feature area
3. State: Observation, `ObservableObject`, TCA, etc.
4. Networking layer already used
5. Test plans/schemes
6. `AGENTS.md`

## Preconditions

- [ ] Deployment target known
- [ ] State pattern known
- [ ] Navigation API in use known (`NavigationStack` vs legacy)
- [ ] Similar screen inspected

## Workflow

1. Trace navigation → view → state → services
2. Plan views/state/tests
3. Implement small composable views; loading/error ([references/conventions.md](references/conventions.md), [references/common-tasks.md](references/common-tasks.md))
4. Verify via `xcodebuild test` / `swift test` as evidenced
5. Report

## Decision rules

1. Deployment target gates API availability
2. Don’t introduce TCA into an ObservableObject app without approval
3. Side effects not inside `body`

## Guardrails

- No secrets in Info.plist committed carelessly
- No bypassing auth gates in UI
- No fabricated verification

## References

- [references/architecture.md](references/architecture.md)
- [references/conventions.md](references/conventions.md)
- [references/common-tasks.md](references/common-tasks.md)
- [references/testing.md](references/testing.md)
- [references/anti-patterns.md](references/anti-patterns.md)

## Output Contract

Targets; files; state pattern; tests; risks.
