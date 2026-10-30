# Detection Signals

Use manifests first, then confirm with source layout.

## Java / Spring / Backbase backend

| Signal | Indicates |
|---|---|
| `pom.xml`, `build.gradle`, `build.gradle.kts` | JVM build |
| `spring-boot-starter-*` | Spring Boot |
| `com.backbase.*` dependencies / BOM | Backbase backend |
| `src/main/java`, `src/test/java` | Standard Maven/Gradle layout |
| `openapi.yaml` / `api.yaml` + BOAT/openapi-generator config | Contract-first API |

Record: JDK toolchain, Spring Boot version, Backbase BOM/version if present.

## TypeScript / Angular / Backbase frontend

| Signal | Indicates |
|---|---|
| `package.json`, `package-lock.json` / `pnpm-lock.yaml` / `yarn.lock` | Node package |
| `@angular/core`, `angular.json` | Angular |
| `nx.json` | Nx monorepo |
| `@backbase/*` packages | Backbase frontend |
| `*.spec.ts`, Playwright/Cypress config | Frontend test stack |

Record: Node engines, Angular version, Backbase frontend package versions, standalone vs NgModule prevalence.

## Other stacks (for recommendation only in first cut)

| Signal | Indicates |
|---|---|
| `requirements.txt` / `pyproject.toml` + FastAPI/Django | Python web |
| `*.csproj` + ASP.NET packages | .NET |
| `build.gradle.kts` + Android plugins | Android / Kotlin |
| `Package.swift` / `*.xcodeproj` | Swift / iOS |

## Guidance files

Check in order: `AGENTS.md` → `.kiro/steering/**` → `.cursor/rules/**` → `CONTRIBUTING.md` → `docs/architecture*`.
