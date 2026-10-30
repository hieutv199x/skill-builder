# Spring Boot — Persistence

Use **only** the persistence technology already on the classpath for the module.

## Spring Data JPA

### Entity guidelines

- Match existing ID strategy (`UUID`, `Long`, sequences)
- Align column naming strategy (`SnakeCase`, quoted identifiers, etc.)
- Prefer lazy associations as the project does; beware N+1 on list endpoints
- Don’t expose entities through controllers when DTO mapping is standard

```java
@Entity
@Table(name = "orders")
public class OrderEntity {
  @Id
  private UUID id;
  // fields...
}
```

### Repositories

```java
public interface OrderRepository extends JpaRepository<OrderEntity, UUID> {
  Optional<OrderEntity> findByCustomerIdAndId(String customerId, UUID id);
}
```

- Derive queries when simple; use `@Query` when neighbors do
- For complex read models, prefer existing projection/JdbcTemplate patterns over huge JPQL

### N+1 & fetch

- Use `JOIN FETCH` / entity graphs / `@EntityGraph` **as already practiced**
- For list APIs, verify similar endpoints don’t lazy-load in a loop
- Don’t add Open Session In View if the project disabled it — respect `spring.jpa.open-in-view`

## JDBC / jOOQ / MyBatis

- Copy the local DAO pattern (named parameters, jOOQ DSL, mapper XML)
- Keep SQL in the same places siblings keep it
- Transactions still belong at the service layer unless the repo uses programmatic TX differently

## Migrations (Flyway / Liquibase)

| Tool | Typical path |
|---|---|
| Flyway | `src/main/resources/db/migration/V<ver>__<desc>.sql` |
| Liquibase | `db/changelog/...` |

Rules:

1. One clear migration per schema change set (follow team numbering)
2. Expand/contract for safe deploys when the estate requires it
3. New NOT NULL columns need default/backfill strategy for existing rows
4. Never `DROP` / destructive changes without explicit approval
5. Don’t mix Flyway and Liquibase
6. Don’t edit applied migrations that already shipped — add a new version

## Transactions — edge cases

- Multi-repository writes → one service-level `@Transactional`
- After-commit side effects: use existing `TransactionSynchronization` / transactional outbox / events pattern — don’t invent a new one
- Catching exceptions inside `@Transactional` may mark rollback — match local handling

## Testing persistence

See [testing.md](testing.md) for `@DataJpaTest` / Testcontainers. Prefer the harness already in the module.
