# Spring Boot — Security

Extend what exists. Do not redesign the security architecture inside a feature.

## Detect the model

| Signal | Meaning |
|---|---|
| `SecurityFilterChain` `@Bean` | Boot 2.7+/3 DSL — extend this |
| `WebSecurityConfigurerAdapter` | Legacy Boot 2 — only if still present; don’t introduce on Boot 3 |
| `spring-boot-starter-oauth2-resource-server` | JWT / opaque resource server |
| `@EnableMethodSecurity` / `@EnableGlobalMethodSecurity` | Method annotations |
| Custom filters | Copy registration order carefully |

## HTTP security changes

When adding a route:

1. Find how sibling routes are authorized
2. Reuse the same matcher style (`antMatchers` legacy vs `requestMatchers`)
3. Prefer **deny-by-default** patterns already configured
4. Never add `permitAll()` to sensitive write/admin APIs for convenience

Illustrative Boot 3 style (adapt to the real chain in-repo):

```java
@Bean
SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
  http
    .authorizeHttpRequests(auth -> auth
      .requestMatchers("/actuator/health").permitAll()
      .requestMatchers(HttpMethod.GET, "/api/public/**").permitAll()
      .anyRequest().authenticated()
    );
  // keep existing oauth2/resource server/session config from the project
  return http.build();
}
```

**Do not replace** the whole chain — surgically add matchers consistent with existing rules.

## Method security

```java
@PreAuthorize("hasAuthority('orders:write')")
public OrderResponse create(CreateOrderRequest request) { ... }
```

- Match expression language already used (`hasRole`, `hasAuthority`, custom beans)
- SpEL must reference authorities that the token/converter actually provides
- Test unauthorized (`401`) and forbidden (`403`) when security is non-trivial

## CSRF / sessions / CORS

- For pure Bearer API services, CSRF may already be disabled — don’t re-enable casually
- For cookie-session apps, preserve CSRF protection
- CORS: extend existing `CorsConfigurationSource`; don’t open `*` with credentials

## Secrets

- Tokens, client secrets, DB passwords → env / secret manager / existing Spring Cloud config
- Never commit real credentials into `application-local.yml` samples without placeholders

## Logging & audit

- Don’t log `Authorization` headers or raw tokens
- If audit events exist, emit them the same way sibling use-cases do
