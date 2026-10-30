# Spring Boot — Common Tasks

Concrete recipes. Adapt names/packages to the repository.

---

## A. Add a REST resource (code-first)

1. **DTOs** — `CreateXRequest`, `XResponse` with Bean Validation  
2. **Mapper** — entity ↔ response (MapStruct or manual)  
3. **Repository** — Spring Data method or JDBC  
4. **Service** — `@Transactional` use-cases; throw domain exceptions  
5. **Controller** — thin; `@Valid`; correct status codes  
6. **Exception mapping** — ensure advice handles new exceptions  
7. **Security** — match sibling route authz  
8. **Tests** — service unit + `@WebMvcTest` or MockMvc slice  
9. **Docs** — springdoc annotations if siblings use them  

---

## B. Add endpoint (API-first / OpenAPI)

1. Edit `openapi.yaml` (paths, schemas, examples, error responses)  
2. Run generator task (`openapi-generator`, BOAT, Maven/Gradle plugin)  
3. Implement generated API interface / delegate  
4. Wire service + persistence  
5. Contract/tests against the spec  
6. Do **not** edit generated files by hand  

---

## C. Add a DB column / table

1. Design nullability + default for existing rows  
2. Write Flyway `V__` / Liquibase changeset  
3. Update entity + DTOs + mapper  
4. Update queries/indexes as needed  
5. `@DataJpaTest` or integration test reading/writing the field  
6. Call out expand/contract / multi-step deploy if required by the estate  

---

## D. Secure a new write API

1. Copy authority/role from the closest write endpoint  
2. Add `@PreAuthorize` / route matcher as local standard  
3. Tests:  
   - no token → `401`  
   - wrong authority → `403`  
   - allowed → `2xx`  
4. Never `permitAll()` “just for local testing” in shared code  

---

## E. Partial update (PATCH)

1. Confirm neighbors use PATCH vs PUT semantics  
2. Prefer explicit patch DTO / JSON Merge Patch / JsonNullable if already used  
3. Don’t null-out omitted fields unless that is the contract  
4. Tests for “field omitted” vs “field set null” if distinguishable  

---

## F. Outbound HTTP call

1. Reuse `RestClient` / `WebClient` / Feign bean style already in the module  
2. Timeouts/retries from existing config  
3. Map upstream 4xx/5xx to domain errors consistently  
4. Unit-test with MockWebServer / WireMock / mocked client — match local practice  
5. No hardcoded base URLs  

---

## G. Publish a domain event / outbox

1. Find existing event publishing pattern (ApplicationEvent, Kafka template, outbox table)  
2. Publish **after** successful state change using the same transactional pattern  
3. Don’t introduce a new broker client for one event  

---

## H. Bugfix in a service method

1. Reproduce with a failing unit/slice test first when feasible  
2. Minimal fix  
3. Keep the regression test  
4. Avoid drive-by refactors in the same change  

---

## I. Pagination / filtering on a list API

1. Copy the estate’s page model (`Page`, `Pageable`, cursor DTO)  
2. Bound `size` max like siblings  
3. Stable sort defaults  
4. Test empty page + second page  
