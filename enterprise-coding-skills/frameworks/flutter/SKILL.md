---
name: flutter-development
description: >-
  Implement and modify Flutter apps: widgets, navigation, state management
  already in use (Bloc/Riverpod/Provider/etc.), and tests. Use when pubspec
  includes the Flutter SDK. Do not introduce a second state library or rewrite
  to native iOS/Android without approval.
metadata:
  version: "1.1.0"
  owner: "platform-engineering"
  category: "framework-development"
  framework: "flutter"
---

# Flutter Development

## Scope

**Allowed:** Dart widgets, routing, state, repositories, golden/widget/unit tests as present.

**Excluded:** Native-only rewrites; adding unused dependencies; committing keystores.

## Detect

1. `pubspec.yaml` SDK constraints + state packages
2. Navigation: GoRouter, Navigator 2, auto_route, etc.
3. State: Bloc, Riverpod, Provider, GetX (match existing only)
4. Theming/localization approach
5. `AGENTS.md`

## Preconditions

- [ ] Dart/Flutter constraints known
- [ ] State + routing known
- [ ] Similar feature inspected

## Workflow

1. Trace widget → state → repository
2. Plan files in existing feature folder layout
3. Implement with loading/error ([references/conventions.md](references/conventions.md), [references/common-tasks.md](references/common-tasks.md))
4. Verify `flutter analyze` / `flutter test`
5. Report

## Decision rules

1. One state management approach per app area
2. Prefer composition of small widgets
3. Don’t block UI isolate with heavy sync work

## Guardrails

- No secrets in source
- No fake analyze/test success

## References

- [references/architecture.md](references/architecture.md)
- [references/conventions.md](references/conventions.md)
- [references/common-tasks.md](references/common-tasks.md)
- [references/testing.md](references/testing.md)
- [references/anti-patterns.md](references/anti-patterns.md)

## Output Contract

Packages; state/routing; analyze/test results; risks.
