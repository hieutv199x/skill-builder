---
name: de-aspnet-core-development
description: >-
  Implement and modify ASP.NET Core Web APIs/MVC: controllers or minimal APIs,
  DI, validation, authz policies, EF Core as used, and tests (xUnit +
  WebApplicationFactory). Use for ASP.NET Core backend work. Do not use for
  Angular/React UI-only tasks. Do not retarget TFMs or rewrite auth as a side
  effect of a feature.
metadata:
  version: "1.1.0"
  owner: "platform-engineering"
  category: "framework-development"
  framework: "aspnet-core"
---

# ASP.NET Core Development

## Scope

**Allowed:** endpoints, DTOs, application services, EF Core changes per team workflow, middleware already patterned, unit/integration tests.

**Excluded:** SPA framework features; silent breaking API changes; TFM upgrades inside feature work.

## Detect

1. `*.csproj`, `Directory.Build.props`, `global.json` → TFM, nullable, analyzers
2. `Program.cs` / `Startup.cs` — minimal hosting vs legacy
3. Controllers vs Minimal APIs prevalence
4. EF Core version; migration assembly
5. Auth: JWT bearer, cookies, policies
6. Validation: DataAnnotations / FluentValidation
7. Tests: xUnit/NUnit/MSTest; WebApplicationFactory
8. `AGENTS.md`

## Preconditions

- [ ] TFM + ASP.NET versions known
- [ ] Endpoint style identified
- [ ] Auth policies identified
- [ ] Similar endpoint inspected

## Workflow

1. Analyze contract + layers
2. Plan endpoint → service → data → tests
3. Implement thin endpoints; reuse problem-details/errors ([references/conventions.md](references/conventions.md), [references/common-tasks.md](references/common-tasks.md))
4. Verify:

```bash
dotnet test --filter FullyQualifiedName~Orders
dotnet build
```

5. Report

## Decision rules

1. Don’t mix Minimal APIs and Controllers in one feature without need
2. Preserve `[Authorize]` / policies
3. EF migrations follow existing workflow only

## Guardrails

- No plaintext secrets in `appsettings`
- No sync-over-async
- No fabricated test results

## References

- [references/architecture.md](references/architecture.md)
- [references/conventions.md](references/conventions.md)
- [references/common-tasks.md](references/common-tasks.md)
- [references/testing.md](references/testing.md)
- [references/anti-patterns.md](references/anti-patterns.md)

## Output Contract

Projects/files; auth; EF/migrations; tests/exit codes; risks.
