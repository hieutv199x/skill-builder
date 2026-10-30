# AGENTS.md Examples

## Good (excerpt — Spring service)

```markdown
# Service Development Instructions

## Identity
- Service: order-service
- Stack: Java 21, Spring Boot 3.3.x (from `pom.xml`)
- Build/test tools: `./mvnw -pl :order-service -am verify`

## Architecture
- Responsibilities: order capture and lifecycle; payments via outbound adapter only
- Entry points: `.../OrderApplication.java`, `.../api/*Controller.java`
- Contracts: `src/main/resources/openapi/order-api.yaml` (API-first; generate before hand-written impl)

## Coding Rules
- MUST: Change public HTTP via OpenAPI + regenerate; do not edit `target/generated-sources/**`
- MUST: Keep authorization on write APIs (`@PreAuthorize` as in `OrderController`)
- SHOULD: Place `@Transactional` on application services, not controllers
- SHOULD: Use MapStruct mappers under `.../mapper`
- MUST NOT: Return JPA entities as REST bodies — use DTOs (avoids lazy-load leaks)
- MUST NOT: Log PANs, tokens, or full PII payloads

## Workflow
- Read `order-api.yaml` before endpoint changes
- Use independent skills: `de-spring-boot-development`, `de-java-development`, `de-testing-strategy`
- Run `./mvnw -pl :order-service -Dtest=... test` before claiming done

## Known Exceptions / Legacy Debt
- `.../batch/LegacyOrderJob.java` uses field injection — LEGACY-ACCEPTED; do not copy

## Evidence
- `pom.xml`, `openapi/order-api.yaml`, `.github/workflows/ci.yml`
- Controllers: `api/OrderController.java`, `api/OrderQueryController.java`
```

## Bad (anti-example — do not emit)

```markdown
## Coding Rules
- MUST: Follow clean code and SOLID always
- MUST: Use the latest Spring Boot APIs
- SHOULD: Write lots of comments
- MUST NOT: Make bugs
## Build
- npm test
```

Why bad: vague, wrong toolchain for a Java service, no paths, no versions, invents commands, no evidence.

## Good (excerpt — Angular app)

```markdown
## Identity
- Service: retail-web
- Stack: Angular 18.2.x, TypeScript 5.x, Nx (from `package.json` / lockfile)
- Build/test tools: `pnpm nx test retail-web`, `pnpm nx lint retail-web`, `pnpm nx build retail-web`

## Coding Rules
- MUST: Match standalone components in `features/**` (do not add NgModules there)
- SHOULD: Use existing design-system table/button components
- MUST NOT: Bypass `authGuard` / entitlement guards on account routes
- MUST NOT: Invent `@backbase/*` selectors not imported elsewhere in this repo
```
