# Backbase Service — Testing

## Prefer

| Layer | Approach |
|---|---|
| Domain/service | Unit + Mockito |
| API | MockMvc / WebTestClient / generated API tests |
| Adapter | Mock SDK/HTTP; mapping assertions |
| Contract | Estate contract plugin if present |
| Full stack | `@SpringBootTest` sparingly + testcontainers if used |

## Fixtures

- Sanitize PII in test payloads
- Reuse golden JSON fixtures from the module
- Don’t commit real customer data dumps

## Commands

Use module-aware wrappers:

```bash
./mvnw -pl :service-name -am -Dtest=FooTest,BarTest test
./gradlew :service-name:test --tests FooTest
```

Record exit codes. Contract goals only when defined (`openapi.generator`, `boat`, etc.).
