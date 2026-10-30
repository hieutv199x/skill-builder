---
name: android-development
description: >-
  Implement and modify Android apps (Kotlin): Compose or View system, ViewModels,
  navigation, repositories, and unit/UI tests as present. Use for Android
  application modules. Do not use for iOS/SwiftUI or pure backend tasks. Do not
  raise minSdk or swap UI toolkits inside a normal feature.
metadata:
  version: "1.1.0"
  owner: "platform-engineering"
  category: "framework-development"
  framework: "android"
---

# Android Development

## Scope

**Allowed:** UI screens, ViewModels/use-cases, navigation, resources, data layer following existing patterns, tests.

**Excluded:** iOS; Gradle plugin/AGP major upgrades as feature side effects; committing keystores.

## Detect

1. AGP, Kotlin, Compose/Material versions; `minSdk`/`targetSdk`
2. UI toolkit: Compose vs XML Views
3. Architecture: MVVM/MVI; Hilt/Dagger/manual DI
4. Navigation component / Compose navigation
5. Networking: Retrofit/Ktor + serialization
6. Modules: `:app`, feature modules
7. Tests: JUnit, Turbine, Espresso/Compose UI tests
8. `AGENTS.md`

## Preconditions

- [ ] SDK levels known
- [ ] Compose vs Views confirmed for the feature area
- [ ] DI and navigation style known
- [ ] Similar screen inspected

## Workflow

1. Trace UI → ViewModel → domain/data
2. Plan screen, state, nav args, repo methods, tests
3. Implement with loading/error; reuse design components ([references/conventions.md](references/conventions.md), [references/common-tasks.md](references/common-tasks.md))
4. Verify Gradle tasks that exist (`:feature:testDebugUnitTest`, etc.)
5. Report

## Decision rules

1. Don’t mix Compose into a Views-only feature module without approval
2. Don’t introduce a second DI framework
3. Keep heavy work off the main thread using existing dispatchers

## Guardrails

- No API keys in source
- No ignoring lifecycle when collecting flows
- No fake test success

## References

- [references/architecture.md](references/architecture.md)
- [references/conventions.md](references/conventions.md)
- [references/common-tasks.md](references/common-tasks.md)
- [references/testing.md](references/testing.md)
- [references/anti-patterns.md](references/anti-patterns.md)

## Output Contract

Modules; SDK assumptions; UI toolkit; tests/commands; risks.
