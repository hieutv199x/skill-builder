# Writing Rules for Backfill

## Voice
- Imperative, agent-facing
- One idea per bullet
- Paths and tool names from **this** repo

## MUST
Hard constraints: authz, contracts, generated sources, secrets, verification.

```text
MUST: Do not edit target/generated-sources/**; change OpenAPI and regenerate.
```

## SHOULD
Preferences when multiple options are valid.

```text
SHOULD: Prefer MapStruct mappers under .../mapper; do not add ModelMapper.
```

## MUST NOT
Always include **why**.

```text
MUST NOT: Return JPA entities from REST controllers — schema leak / lazy-load risk (use DTOs).
```

## Avoid
- Vague “write clean code”
- “Use latest framework APIs” without version pin
- Commands not present in CI/scripts
- Promoting legacy as SHOULD
