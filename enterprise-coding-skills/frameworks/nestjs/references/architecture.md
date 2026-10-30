# NestJS — Architecture

Prefer the structure already evidenced in the target repository. Typical healthy layout:

```text
src/
  main.ts                 # bootstrap, global pipes/filters
  app.module.ts           # root imports only
  config/                 # ConfigModule factories (if present)
  common/                 # shared guards, filters, interceptors, decorators
  <feature>/
    <feature>.module.ts
    <feature>.controller.ts
    <feature>.service.ts
    dto/
    entities/ or domain/  # match repo naming
    <feature>.controller.spec.ts
    <feature>.service.spec.ts
test/                     # e2e (if used)
```

Monorepo (`nest-cli` apps/libs): change the correct `apps/<service>` or `libs/<lib>`; do not dump feature code into the wrong package.

## Layering rules

| Layer | Responsibility | Must not |
|---|---|---|
| Controller | HTTP mapping, status codes, DTO bind | Business rules, direct DB calls |
| Service | Use-cases, domain rules, transactions orchestration | Framework HTTP types when avoidable |
| Repository / Prisma / TypeORM repo | Persistence | HTTP concerns |
| Guard / Pipe / Interceptor | Cross-cutting | Feature-specific business branching (keep rare) |

## Module boundaries

- Import only what the feature needs; export only what other modules must consume
- Avoid circular module imports — extract a shared module if two features need the same provider
- Register `TypeOrmModule.forFeature([...])` / Prisma provider in the feature module that owns the model

## Error & response shape

- Reuse existing `HttpException` subclasses / domain exceptions / exception filters
- Do not invent a new error envelope if the API already has one
- Map domain “not found” / “conflict” to the status codes neighboring endpoints use
