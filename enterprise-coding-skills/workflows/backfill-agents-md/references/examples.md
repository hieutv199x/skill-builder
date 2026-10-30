# Backfill Examples

## Good Identity + Workflow excerpt

```markdown
## Identity
- Service: payment-api
- Stack: Java 21, Spring Boot 3.3.x (`pom.xml`)
- Build/test tools: `./mvnw -pl :payment-api -am verify`

## Workflow
- Read `src/main/resources/openapi/payment-api.yaml` before HTTP changes
- Skills: `spring-boot-development`, `java-development`, `testing-strategy`
- Run targeted `./mvnw -pl :payment-api -Dtest=... test` before done
```

## Good MUST NOT

```markdown
- MUST NOT: Hand-edit `target/generated-sources/**` — regenerate from OpenAPI
- MUST NOT: Log PANs or auth tokens — use correlation ids only
```

## Bad backfill (reject)

```markdown
- MUST: Follow clean architecture always
- SHOULD: Use the newest Angular features
- Build: npm run test
```

Problems: vague, wrong stack for a Java service, invented/unverified commands.

## Merge note example (in report, not AGENTS.md)

```text
Kept: MUST about not committing .env (owner process + still true)
Revised: Java 17 → 21 per pom.xml toolchain
Removed: SHOULD "use Field injection for quicker tests" — reclassified BAD
Added: MUST NOT return entities as JSON
```
