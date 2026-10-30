# Spring Boot — Anti-Patterns

Do **not** copy these even if they appear in legacy modules. Label them `BAD` or `LEGACY-ACCEPTED` in AGENTS.md instead of spreading them.

| Smell | Why it hurts | Do instead |
|---|---|---|
| Business logic in controllers | Untestable HTTP layer; duplicated rules | Application/domain services |
| Fat “god” services | Impossible change isolation | Split by use-case / aggregate |
| Returning JPA entities as JSON | Accidental schema leaks; lazy-load bombs | Response DTOs / projections |
| Field injection (`@Autowired` on fields) | Harder tests; hidden deps | Constructor injection |
| Catch-and-ignore / empty `catch` | Silent data corruption | Map to domain/API errors |
| `@Transactional` on controllers | Wrong boundary; proxy surprises | Service-layer transactions |
| Self-invocation of `@Transactional` methods | Proxy skipped → no TX | Move method to another bean |
| N+1 selects in list APIs | Latency/DB load | Join fetch / graphs / query as neighbors |
| Open-in-view used to hide layering bugs | Unpredictable TX/request coupling | Proper fetch in service/repo |
| String-concatenated SQL | Injection risk | Bound parameters / jOOQ / named params |
| Second ORM beside JPA | Ops & consistency cost | Extend current persistence |
| New mapper library beside MapStruct/manual | Dual styles forever | Stick to the standard |
| `permitAll()` on sensitive writes | Auth holes | Proper authorities/roles |
| Disabling security tests | Regressions ship | Keep 401/403 coverage |
| Logging tokens/PII | Incidents | Redact; log identifiers only |
| Secrets in `application.yml` | Credential leaks | Env / secret store |
| Hand-editing generated OpenAPI code | Overwritten on regen | Edit spec + generator config |
| Mixing `javax.*` and `jakarta.*` | Boot 2/3 breakage | Match Boot major |
| Adding WebFlux to MVC app “for one call” | Dual stacks | Use existing HTTP client pattern |
| Boot/Java upgrade inside feature PR | Unreviewable risk | Separate upgrade change |
| Claiming tests passed without running | False confidence | Execute + record exit codes |
| Deleting failing tests to go green | Hides defects | Fix root cause or quarantine with approval |
| Copying another service’s unverified pattern as estate law | Wrong abstractions | Prefer local healthy evidence |

## Legacy handling

If you must touch a BAD area:

1. Minimal fix only  
2. Don’t expand the anti-pattern  
3. Note remediation follow-up in the report  
4. Don’t “clean up” the whole class unless asked (scope control)  
