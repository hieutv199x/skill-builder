---
name: de-backbase-service-development
description: >-
  Implement or change Backbase Java/Spring backend services in depth: OpenAPI
  or BOAT contract-first flows, resources/controllers, application services,
  integration adapters, entitlements/security hooks, persistence aligned with
  the service, and tests. Use for Backbase SDK backend and service integration
  tasks. Do not use for Angular-only UI. Never invent unsupported Backbase SDK
  methods — verify from BOM/manifests and in-repo usage. Enterprise-proposed
  skill, not an official Backbase distribution.
metadata:
  version: "1.2.0"
  owner: "platform-engineering"
  category: "framework-development"
  framework: "backbase-backend"
---

# Backbase Service Development

## Scope

**Allowed**
- Focused changes to existing Backbase backend services
- API/resource layer (often OpenAPI-driven)
- Application/domain services and validation
- Outbound integration adapters reusing existing clients
- Contract updates following the estate’s BOAT/OpenAPI workflow
- Security/entitlement wiring **consistent with neighboring services**
- Persistence/migrations using the service’s existing stack
- Unit, slice, integration, and contract tests the repo already supports

**Excluded**
- Angular / Backbase Angular UI → `de-backbase-angular-development`
- Embedding proprietary Backbase source/docs into shared skills
- Guessing SDK method names or payload shapes
- Unapproved breaking public API or cross-service contract changes
- Boot/Backbase BOM major upgrades inside a business feature
- Inventing a parallel HTTP/SDK client stack

**Compose with** `de-spring-boot-development` for general Spring layering, testing styles, and JPA/Security mechanics. Prefer **this** skill whenever `com.backbase.*` / banking-service boundaries are in scope.

## Detect

| # | Check | Evidence |
|---|---|---|
| 1 | Build | `pom.xml` / `build.gradle(.kts)`, wrappers |
| 2 | JDK / Spring Boot | toolchain + Boot parent/BOM |
| 3 | Backbase BOM / products | `com.backbase.*` dependencyManagement / imports |
| 4 | Direct Backbase deps | Listed `com.backbase.*` artifacts actually used |
| 5 | Contracts | `openapi.yaml`, `specs/`, `src/main/resources/**` |
| 6 | Generator | BOAT / openapi-generator / Maven-Gradle plugin config |
| 7 | Generated boundary | `target/generated-sources`, `build/generated`, marked packages |
| 8 | Layering | `api`/`rest`, `service`, `mapper`, `adapter`/`outbound`, `persistence` |
| 9 | Security | OAuth2 resource server, entitlement checks, method security |
| 10 | Integration style | existing Feign/WebClient/SDK adapters for same upstreams |
| 11 | Tests | JUnit, MockMvc, SpringBootTest, WireMock, contract tests |
| 12 | Guidance | `AGENTS.md`, estate ADRs, CONTRIBUTING |

**UNVERIFIED rule:** If a Backbase SDK type/method is not imported by compiling code/tests in this repo (or approved licensed docs you may use), mark it `UNVERIFIED` and **stop** — do not invent.

Read [references/sdk-compatibility.md](references/sdk-compatibility.md) and [references/contracts-and-boat.md](references/contracts-and-boat.md).

## Preconditions

- [ ] JDK + Spring Boot + Backbase BOM/product versions recorded
- [ ] Spec path + generator command identified (or confirmed code-first)
- [ ] Generated vs hand-written packages identified
- [ ] Authz/entitlement pattern for target operations identified
- [ ] Similar endpoint **and** adapter inspected (healthy vs BAD)
- [ ] Cross-service contract owners/approvals known if breaking
- [ ] Test commands for module known

## Workflow

### 1. Analyze
Map requirement → public operation → application use-case → downstream systems.  
Read [references/architecture.md](references/architecture.md). Flag smells via [references/anti-patterns.md](references/anti-patterns.md).

### 2. Plan
List:
1. Spec/operation IDs (if contract-first)
2. Generator regen step
3. Hand-written service/adapter/mapper/tests
4. Security annotations/filters to reuse
5. Migration notes if persistence changes
6. Approvals needed for contract breaks

### 3. Implement
1. **Contracts first** when required — [references/contracts-and-boat.md](references/contracts-and-boat.md)
2. Hand-written business logic only outside generated sources
3. Adapters — [references/adapters-and-integration.md](references/adapters-and-integration.md)
4. Security/entitlements — [references/security-and-entitlements.md](references/security-and-entitlements.md)
5. Conventions — [references/coding-conventions.md](references/coding-conventions.md)
6. Recipes — [references/common-tasks.md](references/common-tasks.md)
7. Spring details as needed via `de-spring-boot-development` skill references

### 4. Verify
Use the service wrappers only:

```bash
./mvnw -pl :payments-service -am -Dtest=PaymentServiceTest,PaymentApiTest test
./mvnw -pl :payments-service -am verify
# or Gradle equivalents present in the repo
```

Contract/plugin goals only if defined in the build. See [references/testing.md](references/testing.md).

### 5. Report
Include UNVERIFIED items, regen commands, and approval needs.

## Decision rules

1. Security/legal > approved contracts > version compatibility > AGENTS.md > healthy in-repo patterns > Spring skill defaults > BAD legacy  
2. Spec/config changes **beat** editing generated outputs  
3. Prefer the existing adapter for an upstream over a new client  
4. Don’t add `com.backbase.*` deps outside BOM alignment without rationale  
5. Don’t copy another service’s pattern as estate law without local evidence  
6. When Spring guidance and Backbase estate guidance conflict on public banking contracts, **estate/contract wins**

| Situation | Choose |
|---|---|
| API-first service | Edit OpenAPI → generate → implement delegate/service |
| Generated package contains stubs | Implement in designated hand-written class only |
| Downstream already wrapped | Extend adapter; don’t call raw SDK from controllers |
| Entitlement annotations on siblings | Copy the same pattern |
| PII fields in payloads | Mask in logs; follow data classification |
| Need new SDK method never used in-repo | `UNVERIFIED` — stop and ask |

## Guardrails

- Never invent Backbase SDK APIs
- Never hand-edit generated sources
- Never log PII, tokens, full payment payloads
- Never bypass authorization/entitlements
- Never commit secrets
- Never assert verification without execution evidence
- Never paste proprietary Backbase documentation into skill files

## References

| When | Read |
|---|---|
| Layers & generated boundaries | [references/architecture.md](references/architecture.md) |
| SDK/BOM policy | [references/sdk-compatibility.md](references/sdk-compatibility.md) |
| OpenAPI / BOAT workflow | [references/contracts-and-boat.md](references/contracts-and-boat.md) |
| Outbound adapters | [references/adapters-and-integration.md](references/adapters-and-integration.md) |
| Authz / entitlements | [references/security-and-entitlements.md](references/security-and-entitlements.md) |
| Code style at boundaries | [references/coding-conventions.md](references/coding-conventions.md) |
| Recipes | [references/common-tasks.md](references/common-tasks.md) |
| Tests | [references/testing.md](references/testing.md) |
| Smells | [references/anti-patterns.md](references/anti-patterns.md) |

## Verification checklist

- [ ] Spec regenerated (if API-first) and hand-written code compiles against it
- [ ] No diffs in generated sources except from generator output
- [ ] Authz/entitlement behavior preserved or explicitly approved
- [ ] Adapter errors mapped to estate error model
- [ ] Targeted tests run with exit codes
- [ ] PII not logged
- [ ] UNVERIFIED SDK usage = none (or listed as blocked)

## Output Contract

```markdown
## Backbase service change report
- JDK / Spring Boot / Backbase BOM (evidenced):
- Specs changed + generator command:
- Generated packages touched by regen only:
- Hand-written files changed:
- Downstream systems / adapters:
- Public contract impact (additive | breaking | none):
- Security / entitlements:
- Tests + commands/exit codes:
- UNVERIFIED items:
- Approvals needed:
```
