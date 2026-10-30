# Spring Boot — Version Compatibility

**Always prefer versions from the target repo’s BOM/lock over this file.**  
This matrix helps you avoid inventing APIs from the wrong generation.

## Detect exact versions

Maven:

```text
spring-boot-starter-parent / spring-boot-dependencies version
java.version / maven.compiler.release / toolchain
```

Gradle:

```text
org.springframework.boot plugin version / BOM
JavaLanguageVersion / toolchain
```

Also check dependencyManagement / platform BOMs that may override Boot’s defaults.

---

## Major lines

| Boot line | Jakarta/Java EE namespace | Baseline Java (typical) | Security config style |
|---|---|---|---|
| **3.3 / 3.4 / 3.5+** | `jakarta.*` | 17+ (often 21 in estates) | `SecurityFilterChain` only |
| **3.0 – 3.2** | `jakarta.*` | 17+ | `SecurityFilterChain` |
| **2.7** (legacy) | `javax.*` | 8–17 depending on estate | Prefer `SecurityFilterChain`; adapter may still exist |
| **≤ 2.6** (legacy) | `javax.*` | varies | Often `WebSecurityConfigurerAdapter` |

Rules:

- Boot 3 → **never** introduce `javax.persistence` / `javax.validation` / `javax.servlet`
- Boot 2 → **don’t** migrate packages to Jakarta inside a feature
- Language features (records, sealed, pattern switch, virtual threads) only if **JDK toolchain** supports them **and** neighbors already use them

---

## Feature API caution by area

### Web MVC

| API / topic | Caution |
|---|---|
| `@RestController` + `@RequestMapping` | Safe across Boot 2/3 |
| `ProblemDetail` helpers | Prefer Boot 3+ / Spring 6 style if the app already uses them |
| Path pattern parsing | Boot 3 uses PathPattern more; copy sibling matchers |

### WebFlux

| API / topic | Caution |
|---|---|
| `WebClient` | Prefer over legacy `WebClient.Builder` misuse; match timeouts |
| `RestTemplate` in WebFlux apps | Avoid unless already established with care |

### Persistence

| API / topic | Caution |
|---|---|
| Hibernate 6 (Boot 3) | Query/type changes vs Hibernate 5 — copy local entity patterns |
| `getById` / `getReferenceById` | Prefer APIs already used (`findById`, `getReferenceById`) |
| `spring.jpa.open-in-view` | Boot defaults may differ by generation — don’t flip casually |

### Validation

| Boot | Package |
|---|---|
| 3.x | `jakarta.validation.*` |
| 2.x | `javax.validation.*` |

### Security

| Topic | Boot 3 | Boot 2.7 |
|---|---|---|
| Config base | `SecurityFilterChain` `@Bean` | Same preferred; adapter deprecated |
| Request matchers | `requestMatchers` | Often `antMatchers` in older code — **match file you edit** |
| Method security | `@EnableMethodSecurity` | `@EnableGlobalMethodSecurity` may still appear |
| CSRF for APIs | Often disabled for Bearer APIs — preserve existing choice | same |
| OAuth2 resource server | `spring.security.oauth2.resourceserver.*` | similar but package/config drift — copy neighbors |

### Observability

| Topic | Guidance |
|---|---|
| Micrometer | Use meters/tags like sibling services |
| Micrometer Tracing / Brave / OTel | Don’t swap tracers in a feature |
| Actuator | Endpoint exposure is environment policy — don’t broaden |

### HTTP clients

| Client | Notes |
|---|---|
| `RestClient` | Spring 6.1+ / newer Boot 3 — only if already on classpath/used |
| `WebClient` | Reactive or blocking retrieve — match existing |
| `RestTemplate` | Legacy but fine if that’s the standard |
| OpenFeign | Keep Feign if present; don’t add Feign beside RestClient casually |

---

## Dependency management

- Add starters that exist in the **same Boot BOM** (don’t pin random Spring versions)
- Align third-party libs with the estate BOM when one exists
- New dependencies require rationale + compatibility note in the change report
- Never force a Boot upgrade to “get” an API for a small feature

---

## Upgrade policy

| Change | Allowed inside feature PR? |
|---|---|
| Feature code on current Boot | Yes |
| Patch dependency bump required by CVE and approved | Only if separately approved |
| Boot 2 → 3 migration | **No** — dedicated upgrade track |
| Java 17 → 21 | **No** — dedicated upgrade track |
| Hibernate 5 → 6 as side effect | **No** |

When the user asks for an upgrade, treat it as its own workflow with a compatibility review — not as part of `implement-feature` for business logic.

---

## Quick “don’t invent” list

Do **not** assume these are available unless manifests show a supporting Boot/JDK:

- `RestClient` on older Boot 2 apps  
- Jakarta packages on Boot 2  
- `@MockitoBean` naming if the suite still uses `@MockBean`  
- Virtual threads (`spring.threads.virtual.enabled`) without evidence  
- Native/AOT hints without an existing Graal/native setup  

When unsure: open a sibling class and copy its imports — that is the ground truth.
