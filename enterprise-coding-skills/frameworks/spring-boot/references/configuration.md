# Spring Boot — Configuration

## Prefer typed properties

If the project uses `@ConfigurationProperties`:

```java
@ConfigurationProperties(prefix = "order")
public record OrderProperties(int maxLines, Duration placeTimeout) {}
```

Register the way neighbors do (`@EnableConfigurationProperties`, `@ConfigurationPropertiesScan`, or `@Bean` + `@EnableConfigurationProperties`).

## Files & profiles

| File | Typical use |
|---|---|
| `application.yml` | Shared defaults |
| `application-local.yml` | Dev overrides (not secrets) |
| `application-k8s.yml` / `prod` | Environment-specific |
| Env vars / mounted secrets | Credentials |

Rules:

- Don’t hardcode environment URLs in Java
- Don’t commit secrets; use placeholders in samples
- Keep property keys stable — renaming is often a deployment break
- Prefer `spring.config.import` / existing external config mechanisms already in use

## Feature flags

If the estate uses LaunchDarkly / custom toggles / Spring Cloud, follow that — don’t invent a parallel flag system for one if/else.

## Actuator

- Don’t expose new sensitive actuator endpoints without approval
- Health contributors: only add if operationally required and consistent with ops practice
