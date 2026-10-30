# Adapters & Integration

## Prefer existing adapters

Before creating a new client:

1. Search for adapters talking to the same upstream
2. Reuse configuration (base URL, auth, timeouts, mappers)
3. Extend mapping for new fields/operations

## Adapter responsibilities

- Translate between domain and upstream DTOs/SDK types
- Map upstream errors → estate domain/API errors
- Propagate correlation/request IDs as siblings do
- Timeout/retry **only** using existing policies

## Resilience

- Copy circuit breaker / retry annotations if the estate standardizes them
- Don’t invent a new resilience library for one call
- Idempotency: follow existing keys/headers for payments-like operations

## Testing adapters

- Unit-test mapping + error translation with mocked SDK/HTTP
- Use WireMock/MockWebServer if that is local practice
- Never hit real banking systems from unit tests
