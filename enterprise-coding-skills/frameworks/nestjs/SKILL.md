---
name: nestjs-development
description: >-
  Implement and modify NestJS Node backends: modules, controllers, providers,
  DTOs/validation, guards, interceptors, pipes, ORM integration (TypeORM/Prisma),
  and Jest unit/e2e tests. Use when package.json includes @nestjs/core or the
  task is NestJS API/service work. Do not use for Angular frontend-only tasks,
  Spring Boot, or inventing microservices/CQRS topology not already in the repo.
metadata:
  version: "1.1.0"
  owner: "platform-engineering"
  category: "framework-development"
  framework: "nestjs"
---

# NestJS Development

## Scope

**Allowed**
- Feature modules: controllers, services/providers, DTOs, entities/models
- Cross-cutting pieces already used in-repo: guards, interceptors, filters, pipes
- Persistence via the ORM already present (TypeORM, Prisma, Mongoose, etc.)
- Config/env wiring consistent with existing `ConfigModule` usage
- Unit tests (`*.spec.ts`) and e2e tests under the repo’s Nest testing layout

**Excluded**
- Angular/React UI implementation
- Greenfield rewrite to microservices, CQRS, or GraphQL when the app is REST monolith
- Major Nest or Node upgrades as a side effect of a feature
- Inventing SDK/client methods not evidenced in the codebase

## Detect

Before editing, record evidence (path + version):

1. **Manifests** — `package.json`, lockfile (`package-lock.json` / `pnpm-lock.yaml` / `yarn.lock`)
2. **Nest version** — `@nestjs/common`, `@nestjs/core`, `@nestjs/platform-express` (or fastify)
3. **Entry** — `src/main.ts`, `src/app.module.ts` (or `apps/<name>` in a monorepo)
4. **HTTP adapter** — Express vs Fastify (`@nestjs/platform-*`)
5. **Validation** — `ValidationPipe` global? `class-validator` / `zod` / custom
6. **ORM** — `@nestjs/typeorm`, `prisma`, `mongoose`, raw `pg` — match existing only
7. **Auth** — `@nestjs/passport`, JWT guards, custom `AuthGuard` patterns
8. **API docs** — `@nestjs/swagger` decorators already used?
9. **Tests** — Jest config, `test/` e2e, `*.spec.ts` next to sources
10. **Guidance** — `AGENTS.md`, `.kiro/steering/`, `.cursor/rules/`

Read [references/version-compatibility.md](references/version-compatibility.md) after detecting versions.

## Preconditions

- [ ] Nest major version known from lockfile
- [ ] One similar feature module inspected (structure + naming)
- [ ] Auth/guard requirements for the endpoint identified
- [ ] DTO/validation approach identified (do not mix styles)
- [ ] Persistence approach identified (do not add a second ORM)
- [ ] Public contract impact assessed (breaking vs additive)

If a precondition is unknown, state the assumption explicitly before coding.

## Workflow

### 1. Analyze
- Map the requirement to routes, payloads, status codes, and side effects
- Find neighboring modules that solve a similar problem; prefer those patterns
- Flag anti-patterns with [references/anti-patterns.md](references/anti-patterns.md) — do not copy them

### 2. Plan
- List files to add/change (module, controller, service, dto, entity/repo, tests)
- Decide: extend existing module vs new feature module ([references/architecture.md](references/architecture.md))
- Note any contract/OpenAPI/Swagger updates required

### 3. Implement
Follow [references/conventions.md](references/conventions.md) and [references/common-tasks.md](references/common-tasks.md):
1. DTOs + validation at the HTTP boundary
2. Controller stays thin — delegate to service
3. Service owns business rules; persistence behind existing repository/adapter style
4. Register providers/controllers in the feature `Module`
5. Reuse existing guards, interceptors, exception filters — do not bypass auth
6. Add Swagger decorators only if the module already uses them

### 4. Verify
Run the **project’s** scripts (do not invent npm script names). Typical patterns:

```bash
npm run lint
npm run test -- --testPathPattern=users
npm run test:e2e -- --testPathPattern=users
npm run build
```

Use `pnpm`/`yarn` when the lockfile says so. See [references/testing.md](references/testing.md).

### 5. Report
Fill the Output Contract. Never claim PASS without exit-code evidence.

## Decision rules

Priority when patterns conflict:

1. Security / authz policy
2. Explicit AGENTS.md / approved contracts
3. Version compatibility (installed Nest major)
4. Healthy similar module in the same repo
5. This skill’s conventions
6. Weak/legacy examples → treat as `LEGACY-ACCEPTED` or `BAD`, do not spread

| Situation | Choose |
|---|---|
| App uses feature modules | Add/extend feature module — not god `AppModule` providers |
| Global `ValidationPipe` exists | Use `class-validator` DTOs; don’t add ad-hoc validation |
| TypeORM already present | Keep TypeORM — don’t add Prisma for one feature |
| Prisma already present | Keep Prisma |
| REST only | Don’t introduce GraphQL resolver layer |
| CQRS folders exist and are the norm | Follow CQRS; otherwise don’t introduce it |
| Similar endpoint uses Swagger | Decorate new endpoints consistently |

## Guardrails

- Never disable or skip global/auth guards to “make the happy path work”
- Never accept untyped `any` bodies when DTO validation is the project standard
- Never commit secrets; never log tokens/PII
- Never edit generated Prisma client by hand — change schema + generate
- Never assert tests/lint/build passed without running them
- Keep public HTTP changes additive unless explicitly approved as breaking

## References

| When | Read |
|---|---|
| New module / layering | [references/architecture.md](references/architecture.md) |
| Naming, DTOs, DI, errors | [references/conventions.md](references/conventions.md) |
| CRUD endpoint, auth-protected route | [references/common-tasks.md](references/common-tasks.md) |
| Unit/e2e patterns | [references/testing.md](references/testing.md) |
| Version / API caution | [references/version-compatibility.md](references/version-compatibility.md) |
| Smells to avoid | [references/anti-patterns.md](references/anti-patterns.md) |

## Verification

Minimum before declaring done:

1. Targeted unit tests for the service (and controller if that is local practice)
2. Lint + typecheck/build if present in `package.json`
3. E2e/supertest for the route when the repo has e2e harness
4. Manual notes for anything skipped (with reason)

## Output Contract

```markdown
## NestJS change report
- Nest / Node versions (evidenced):
- Modules/files changed:
- Public routes impacted (method + path + breaking?):
- Auth/guards applied:
- Persistence touchpoints:
- Tests added/updated:
- Commands run + exit codes:
- Assumptions / unresolved risks:
- Approvals needed:
```
