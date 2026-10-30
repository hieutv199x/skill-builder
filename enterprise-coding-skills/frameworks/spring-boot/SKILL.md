---
name: spring-boot-development
description: >-
  Implement and modify Spring Boot / Java services in depth: REST/WebFlux
  endpoints, DTO validation, application services, JPA/JDBC/jOOQ persistence,
  transactions, Flyway/Liquibase, Spring Security, OpenAPI-first flows, Problem
  Details errors, and tests (JUnit 5, MockMvc, WebTestClient, Testcontainers).
  Use when pom.xml or Gradle includes spring-boot-starter. Do not use for
  Angular/UI-only work or Backbase-specific SDK tasks (use
  backbase-service-development). Never invent Spring APIs unsupported by the
  Boot/JDK versions installed in the repo.
metadata:
  version: "1.2.0"
  owner: "platform-engineering"
  category: "framework-development"
  framework: "spring-boot"
---

# Spring Boot Development

## Scope

**Allowed**
- Web layer: `@RestController` / functional WebFlux handlers as used by the app
- Application/domain services, mappers, validators
- Persistence: Spring Data JPA, JDBC, jOOQ, MyBatis — **only the stack already present**
- Schema changes via Flyway/Liquibase using the repo’s migration workflow
- Security wiring that **extends** existing `SecurityFilterChain` / method security
- Config properties, actuators usage consistent with the service
- Focused unit/slice/integration tests and contract updates when API-first
- Observability hooks (Micrometer/tracing) only when matching existing patterns

**Excluded**
- Frontend (Angular/React/etc.)
- Backbase SDK-specific work → `backbase-service-development`
- Boot major / JDK major upgrades as a side effect of a feature
- Introducing a second persistence stack, mapper stack, or security framework
- Unapproved breaking public API / DB destructive changes
- Inventing Spring APIs from a newer Boot than the lock/BOM shows

## Detect

Before any edit, record **path + version evidence**:

| # | Check | Where to look |
|---|---|---|
| 1 | Build system | `pom.xml`, `build.gradle`, `build.gradle.kts`, wrappers `mvnw`/`gradlew` |
| 2 | JDK | `maven.compiler.release`, `java.version`, `toolchain`, CI image |
| 3 | Spring Boot | parent/BOM `spring-boot-starter-parent` or `org.springframework.boot` version |
| 4 | Namespace | `jakarta.*` (Boot 3+) vs `javax.*` (Boot 2.x legacy) |
| 5 | Web stack | `spring-boot-starter-web` (MVC) vs `spring-boot-starter-webflux` |
| 6 | Persistence | `spring-data-jpa`, JDBC, jOOQ, MyBatis starters/deps |
| 7 | Migrations | `db/migration` (Flyway), `db/changelog` (Liquibase) |
| 8 | Security | `spring-boot-starter-security`, OAuth2 Resource Server, method security |
| 9 | API-first | `openapi.yaml` / `api.yaml`, `openapi-generator`, springdoc, BOAT |
| 10 | Mapping | MapStruct, hand mappers, ModelMapper (match existing only) |
| 11 | Errors | `problem-spring-web`, `@ControllerAdvice`, custom error JSON |
| 12 | Tests | JUnit 5, MockMvc, WebTestClient, `@DataJpaTest`, Testcontainers, REST Assured |
| 13 | Guidance | `AGENTS.md`, `.kiro/steering/`, `.cursor/rules/`, CONTRIBUTING |

Then read [references/version-compatibility.md](references/version-compatibility.md).

Optionally inspect 1–3 sibling endpoints end-to-end (controller → service → repo → test) and classify patterns GOOD / LEGACY-ACCEPTED / BAD before copying anything.

## Preconditions

- [ ] Boot + JDK versions recorded (not guessed)
- [ ] MVC vs WebFlux confirmed for the module you edit
- [ ] Persistence + migration tool identified (or N/A)
- [ ] Authn/authz pattern for the target routes identified
- [ ] Error/response envelope identified
- [ ] DTO/validation + mapper style identified
- [ ] Public contract impact classified: additive / breaking / internal-only
- [ ] Test command for a narrow slice known (`./mvnw -Dtest=…` or Gradle equivalent)

If something is unknown, **state the assumption** in the plan before coding.

## Workflow

### 1. Analyze
- Map requirement → HTTP contract (status, body, headers) → application use-case → persistence/events
- Find the closest healthy neighbor feature; prefer it over generic tutorials
- Reject smells in [references/anti-patterns.md](references/anti-patterns.md)

### 2. Plan
List the minimal file set, typically:
1. OpenAPI / external contract (if API-first)
2. Request/response DTOs + validation
3. Controller (or generated interface impl)
4. Service (+ transaction boundaries)
5. Entity/row type + repository / JDBC
6. Migration (if schema changes)
7. Mapper
8. Tests (service + web slice at minimum when risk warrants)
9. Security config **only if** new paths/roles are required

Read [references/architecture.md](references/architecture.md) when adding packages/modules.

### 3. Implement (order matters)
1. **Contract first** when the repo is API-first — see [references/api-and-errors.md](references/api-and-errors.md)
2. DTOs + `@Valid` / `@Validated` at the boundary — [references/coding-conventions.md](references/coding-conventions.md)
3. Thin controller → service use-case
4. Persistence + migration — [references/persistence.md](references/persistence.md)
5. Reuse existing exception handling / Problem Details
6. Extend security carefully — [references/security.md](references/security.md)
7. Config via existing `@ConfigurationProperties` style — [references/configuration.md](references/configuration.md)
8. Follow recipes in [references/common-tasks.md](references/common-tasks.md)

### 4. Verify
Use **wrappers and modules that exist in the repo**. Examples:

```bash
# Maven
./mvnw -Dtest=OrderServiceTest,OrderControllerTest test
./mvnw -pl :order-service -am -Dtest=OrderServiceTest test
./mvnw -DskipTests compile

# Gradle
./gradlew :order-service:test --tests OrderServiceTest
./gradlew test
./gradlew check
```

Prefer the narrowest meaningful tests first, then module build. Details: [references/testing.md](references/testing.md).

**Never** claim PASS without exit-code evidence. If a check is skipped, say why.

### 5. Report
Fill the Output Contract. Call out breaking changes and required approvals.

## Decision rules

Priority when guidance conflicts:

1. Security / legal / compliance  
2. Explicit approved public contracts  
3. Version compatibility (installed Boot/JDK)  
4. `AGENTS.md` / validated project guidance  
5. Healthy in-repo neighbor patterns  
6. This skill’s conventions  
7. Legacy BAD patterns → document, do **not** spread  

| Situation | Choose |
|---|---|
| Boot 3.x | `jakarta.*` only — never mix `javax.*` |
| Boot 2.x legacy | `javax.*`; don’t “modernize” mid-feature unless asked |
| `starter-web` app | Spring MVC — don’t add WebFlux controllers casually |
| `starter-webflux` app | Reactive types end-to-end — don’t block with JDBC without existing pattern |
| OpenAPI is source of truth | Edit spec → generate → implement; don’t hand-diverge DTOs |
| Code-first + springdoc | Update annotations/DTOs consistently with neighbors |
| MapStruct present | Keep MapStruct — don’t add ModelMapper |
| Manual mappers present | Keep manual — don’t add MapStruct for one field |
| Flyway present | Flyway only — don’t introduce Liquibase |
| JPA standard | Don’t add jOOQ/MyBatis for one query without approval |
| Security DSL present | Extend `SecurityFilterChain` bean — don’t revive `WebSecurityConfigurerAdapter` on Boot 3 |
| Similar endpoint uses `@PreAuthorize` | Match it; don’t invent a parallel filter unless required |

## Guardrails

- Never commit secrets or local passwords in `application-*.yml`
- Never log passwords, tokens, full PANs, or raw sensitive payloads
- Never widen security with `permitAll()` / disabled CSRF on sensitive state-changing APIs without explicit approval
- Never hand-edit generated OpenAPI sources — change spec/config
- Never put business rules in controllers or repositories
- Never return JPA entities as API bodies when DTOs are the project norm
- Never upgrade Spring Boot / Java inside a feature PR
- Never assert tests/lint/build succeeded without running them

## References

| When | Read |
|---|---|
| Packages, layers, module layout | [references/architecture.md](references/architecture.md) |
| Naming, DI, DTOs, transactions, code samples | [references/coding-conventions.md](references/coding-conventions.md) |
| REST, validation, Problem Details, OpenAPI | [references/api-and-errors.md](references/api-and-errors.md) |
| JPA/JDBC, migrations, transactions | [references/persistence.md](references/persistence.md) |
| SecurityFilterChain, method security | [references/security.md](references/security.md) |
| Config properties, profiles | [references/configuration.md](references/configuration.md) |
| Step-by-step feature recipes | [references/common-tasks.md](references/common-tasks.md) |
| Unit/slice/integration tests | [references/testing.md](references/testing.md) |
| Boot/JDK/Security version matrix | [references/version-compatibility.md](references/version-compatibility.md) |
| What not to copy | [references/anti-patterns.md](references/anti-patterns.md) |

## Verification checklist

Before declaring done:

- [ ] Targeted unit/slice tests for the change (or documented gap)
- [ ] Compile/test command(s) executed with exit codes recorded
- [ ] Migration reviewed if schema changed (nullability/defaults for existing rows)
- [ ] Authz behavior preserved or explicitly approved
- [ ] Public contract diff summarized (additive vs breaking)
- [ ] No new dependency without rationale + Boot BOM alignment

## Output Contract

```markdown
## Spring Boot change report
- JDK / Spring Boot (evidenced):
- Web stack (MVC | WebFlux):
- Persistence / migrations touched:
- Files changed:
- Public API / contract impact (additive | breaking | none):
- Security / authz notes:
- Tests added/updated:
- Commands run + exit codes:
- Skipped checks + reason:
- Assumptions:
- Approvals needed:
```
