# Backbase Service — Coding Conventions

Apply Spring conventions from `de-spring-boot-development`, plus:

## Boundaries

- No SDK types in controllers if adapters/mappers exist — keep API models stable
- Map early at adapter edges
- Keep transaction boundaries on application services

## Naming

Match the service:
- `*Api` / `*Controller` / `*Resource`
- `*Service` / `*UseCase`
- `*Adapter` / `*Client`
- `*Mapper` (MapStruct common in estates)

## Validation

- Validate at API boundary with the estate’s standard (Bean Validation, custom validators)
- Align with OpenAPI constraints when API-first

## Logging

```text
OK:  orderId, arrangementId, correlationId
BAD: PAN, tokens, passwords, full PII payloads, raw auth headers
```

## Errors

Reuse the service’s problem/error model — don’t invent a second envelope for one endpoint.
