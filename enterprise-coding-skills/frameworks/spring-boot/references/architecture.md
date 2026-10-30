# Spring Boot — Architecture

Prefer the structure already evidenced in the target repository. Do not impose a new packaging style in a feature change.

## Typical healthy layering

```text
web / api          Controllers, request/response DTOs, assemblers
        ↓
application        Use-case services, orchestration, transactions
        ↓
domain             Business rules, domain models (when present)
        ↓
persistence / adapters   JPA entities, repositories, JDBC, external HTTP clients
```

Multi-module example:

```text
order-service/
  order-api/           # optional API models / OpenAPI
  order-domain/
  order-application/
  order-infrastructure/
  order-bootstrap/     # @SpringBootApplication
```

If the repo is a single module (`src/main/java/...`), keep **feature packages** or **technical layers** consistent with neighbors — don’t reshuffle the whole tree.

## Package styles (pick what the repo uses)

| Style | Example | When |
|---|---|---|
| Feature / vertical | `com.example.order.api`, `.service`, `.persistence` | Modern services |
| Technical layers | `controller`, `service`, `repository` at top level | Older codebases |
| Hexagonal | `domain`, `application`, `adapter.in`, `adapter.out` | Explicit ports/adapters |

## Layer responsibilities

| Layer | Does | Must not |
|---|---|---|
| Controller | Map HTTP ↔ use-case; status codes; call validation | Business rules; open transactions; call `EntityManager` directly |
| Service | Use-cases; invariants; transaction boundary | HTTP types (`HttpServletRequest`) when avoidable |
| Repository / DAO | Persistence I/O | Authorization decisions; HTTP mapping |
| Entity / table model | Persistence shape | Accidental public API (unless project intentionally exposes it) |
| `@ControllerAdvice` | Map exceptions → stable error body | Swallow unexpected errors silently |

## Bean & configuration placement

- `@SpringBootApplication` stays in the bootstrap module/package already used
- `@Configuration` / `@Enable…` follow existing config packages
- Don’t create a second `Application` class
- Component scan must continue to cover new packages — place code inside scanned roots

## Integration boundaries

- Outbound HTTP: reuse existing `RestClient` / `WebClient` / OpenFeign style
- Messaging: reuse existing Kafka/Rabbit templates and error handlers
- Prefer anti-corruption adapters when talking to external systems if that pattern exists

## When adding a new capability

1. Place it next to the closest sibling feature
2. Export only what other modules already expect (avoid new public cross-module APIs without need)
3. Keep generated sources (OpenAPI) separated from hand-written code as the repo already does
