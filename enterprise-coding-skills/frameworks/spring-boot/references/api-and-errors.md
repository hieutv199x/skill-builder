# Spring Boot — API & Errors

## REST style

Mirror neighboring APIs for:

- Path prefix (`/api`, `/api/v1`, context path)
- Resource naming (nouns, pluralization)
- Status codes (`201` + body vs `201` + `Location`, `204` on delete)
- Idempotency headers if already used
- Pagination (`page`/`size` vs cursor) — copy the existing model

### Typical status mapping

| Outcome | Status |
|---|---|
| Created | `201 Created` |
| Updated OK | `200` or `204` (match neighbors) |
| Deleted | `204` or `200` |
| Validation failure | `400` / `422` (match existing) |
| Unauthenticated | `401` |
| Forbidden | `403` |
| Missing resource | `404` |
| Conflict | `409` |

## OpenAPI / API-first

When specs are the source of truth:

1. Update the OpenAPI document
2. Run the project’s generator (openapi-generator, BOAT, etc.)
3. Implement generated API interfaces / delegates
4. **Do not** hand-edit generated sources
5. Keep examples/schemas aligned with validation annotations

When code-first + springdoc-openapi:

- Annotate new endpoints like siblings (`@Operation`, `@ApiResponse`)
- Keep schema names stable — renaming is often breaking for clients

## Validation

- Trigger with `@Valid` / `@Validated` on `@RequestBody`, `@RequestParam`, `@PathVariable` as needed
- Custom validators live next to existing constraint annotations
- Prefer meaningful messages already localized/styled by the service

## Error envelope

**Prefer the existing `@ControllerAdvice` / Problem Details setup.**

RFC 7807-style example (only if the service already uses Problem Details):

```json
{
  "type": "https://example.com/problems/order-not-found",
  "title": "Order not found",
  "status": 404,
  "detail": "Order 123 was not found",
  "instance": "/api/orders/123"
}
```

Rules:

- Don’t invent a second error JSON shape beside the standard one
- Map domain exceptions → HTTP in one place (`@ExceptionHandler`)
- Don’t leak stack traces or SQL to clients in non-dev profiles
- Preserve correlation/request IDs if the advice already sets them

## Domain exceptions

```java
public class OrderNotFoundException extends RuntimeException {
  public OrderNotFoundException(String id) {
    super("Order not found: " + id);
  }
}
```

Extend existing base types (`BusinessException`, `NotFoundException`, …) when present instead of creating parallel hierarchies.
