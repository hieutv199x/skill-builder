# Writing MUST / SHOULD / MUST NOT

## Voice

- Imperative, agent-addressed: “Do X”, “Do not Y”
- Specific to **this** repo (paths, tools, versions)
- One idea per bullet
- Include evidence hint when non-obvious: `(see src/... )`

## MUST (hard constraints)

Use for:
- Authz must not be weakened
- Public contract / generated sources policy
- Secrets handling
- Required verification before done
- Namespace/version constraints (e.g. jakarta-only on Boot 3)

Bad MUST: “Write clean code.”  
Good MUST: “Do not edit files under `target/generated-sources/`; change OpenAPI and regenerate.”

## SHOULD (preferences)

Use when multiple approaches work but one matches the service:
- Mapper style, package layout, test style, logging fields

Bad SHOULD: “Prefer best practices.”  
Good SHOULD: “Prefer MapStruct mappers in `...mapper` packages; do not introduce ModelMapper.”

## MUST NOT (prohibitions)

Always add **reason**:

```text
- MUST NOT: Return JPA entities from REST controllers — leaks schema and triggers lazy-load errors (use DTOs; see OrderController).
```

## Anti-patterns in AGENTS.md itself

| Bad AGENTS writing | Fix |
|---|---|
| 40 vague bullets | Cut to ≤7 per section; keep only enforceable rules |
| Copy-pasted Spring Boot textbook | Keep only rules evidenced here |
| Commands that don’t exist in CI | Delete or fix from package scripts |
| “Always use latest Angular APIs” | Pin to detected major |
| Promoting legacy as SHOULD | Move to Legacy Debt |
| No Evidence section | Add paths |

## Size budget

Aim for a file an agent can load usefully: roughly **80–180 lines**. If longer, split monorepo packages or move essays to `docs/` and link them.
