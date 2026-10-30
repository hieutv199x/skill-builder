# NestJS — Anti-Patterns

Do **not** copy these even if they appear in legacy modules (label `BAD` / `LEGACY-ACCEPTED` in AGENTS.md instead):

| Smell | Why it hurts | Do instead |
|---|---|---|
| Business logic in controllers | Untestable HTTP layer | Delegate to services |
| `any` / unvalidated `@Body()` | Injection & corrupt data | DTO + ValidationPipe / Zod |
| Second ORM beside the standard | Ops & consistency cost | Extend existing persistence |
| Bypassing guards with duplicate “internal” routes | Auth holes | Reuse guards; explicit admin policy |
| Circular module imports | Runtime DI failures | Shared kernel module |
| Catch-all `try/catch` returning 200 | Hides failures | Let filters map domain errors |
| Request-scoped everything | Perf & complexity | Default scope unless required |
| Editing generated Prisma client | Overwritten on generate | Schema + generate |
| God `AppModule` with all providers | No boundaries | Feature modules |
| Claiming tests passed without running | False confidence | Execute and record exit codes |
| Logging passwords/tokens | Security incident | Redact; structured logs |
| Mixing CQRS/Event sourcing into a simple CRUD app | Accidental complexity | Match existing style |
