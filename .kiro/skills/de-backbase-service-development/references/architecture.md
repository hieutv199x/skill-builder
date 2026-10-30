# Backbase Service — Architecture

Process-level guidance. Confirm package names in the target repository.  
Compose with `de-spring-boot-development` for generic Spring layering.

## Typical concerns

```text
API / resource          OpenAPI operations, request/response models
        ↓
Application services    Use-cases, orchestration, validation
        ↓
Domain (optional)       Banking rules local to the service
        ↓
Adapters outbound       Backbase/product SDK clients, HTTP, messaging
Persistence             DB via the service’s existing stack
```

## Generated vs hand-written

| Kind | Location (examples) | Edit? |
|---|---|---|
| OpenAPI / specs | `src/main/resources/openapi/`, `specs/` | Yes (source of truth when API-first) |
| Generated stubs/clients | `target/generated-sources`, `build/generated` | **No** — regen only |
| Hand-written delegates/services | `.../service`, `.../api/impl` | Yes |
| Outbound adapters | `.../adapter`, `.../outbound`, `.../client` | Yes |

## Boundaries

- Controllers/resources stay thin
- Controllers do **not** call remote SDKs directly when an adapter layer exists
- Cross-service calls go through existing integration patterns (timeouts, error mapping, correlation IDs)
- Shared libraries: only use published estate artifacts already on the classpath
