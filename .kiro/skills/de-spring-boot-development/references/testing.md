# Spring Boot — Testing

Detect first: JUnit 5, AssertJ/Hamcrest, Mockito, MockMvc vs WebTestClient, `@SpringBootTest`, Testcontainers, fixtures.

## Choose the right test type

| Risk / layer | Prefer | Annotation / tool |
|---|---|---|
| Pure domain logic | Unit | Plain JUnit + Mockito |
| Web mapping + validation | Web slice | `@WebMvcTest` + MockMvc **or** WebTestClient (WebFlux) |
| JPA mapping/queries | Persistence slice | `@DataJpaTest` |
| Security expressions | Web slice with security | `@WebMvcTest` + `@WithMockUser` / `@WithSecurityContext` |
| Multi-bean wiring / DB | Integration | `@SpringBootTest` + Testcontainers if used |
| Public contract | Contract | Spring Cloud Contract / OpenAPI tests if present |

Don’t jump to full `@SpringBootTest` when a slice test matches local practice and gives enough confidence.

## Service unit test sketch

```java
@ExtendWith(MockitoExtension.class)
class OrderServiceTest {
  @Mock OrderRepository orderRepository;
  @Mock OrderMapper orderMapper;
  @InjectMocks OrderService orderService;

  @Test
  void getById_whenMissing_throwsNotFound() {
    when(orderRepository.findById("x")).thenReturn(Optional.empty());
    assertThatThrownBy(() -> orderService.getById("x"))
        .isInstanceOf(OrderNotFoundException.class);
  }
}
```

Use AssertJ if the module already does; otherwise match existing assertions.

## `@WebMvcTest` sketch (MVC)

```java
@WebMvcTest(OrderController.class)
class OrderControllerTest {
  @Autowired MockMvc mockMvc;
  @MockBean OrderService orderService;

  @Test
  void get_returns200() throws Exception {
    when(orderService.getById("1")).thenReturn(new OrderResponse("1", "OK"));

    mockMvc.perform(get("/api/orders/{id}", "1").accept(MediaType.APPLICATION_JSON))
        .andExpect(status().isOk())
        .andExpect(jsonPath("$.id").value("1"));
  }

  @Test
  void create_whenInvalid_returns400() throws Exception {
    mockMvc.perform(post("/api/orders")
            .contentType(MediaType.APPLICATION_JSON)
            .content("{}"))
        .andExpect(status().isBadRequest());
  }
}
```

Notes:

- `@WebMvcTest` loads a narrow context — import security test config the way siblings do
- `@MockBean` vs `@MockitoBean` (Boot 3.4+) — **copy whatever the repo uses**
- For JSON asserts, prefer existing `jsonPath` / JSONAssert style

## WebFlux

Use `WebTestClient` bound to the controller/router function. Don’t use MockMvc on a WebFlux-only app.

## `@DataJpaTest`

- Use when verifying entity mapping, custom `@Query`, or constraints
- Prefer Testcontainers if the module already rejects H2 dialect differences
- Import only required entities; follow existing `@Import` / `@AutoConfigureTestDatabase` patterns

## Security tests

```java
@Test
@WithMockUser(authorities = "orders:read")
void get_whenAuthorized_returns200() { ... }

@Test
@WithMockUser(authorities = "orders:read")
void create_whenForbidden_returns403() { ... }
```

If the app uses JWT converters, prefer the project’s security test support classes over inventing token strings.

## Testcontainers

Use only when already on the test classpath / Surefire config. Reuse shared containers/fixtures from test source sets — don’t spin unique containers per class if the suite has a shared module.

## Commands (record exact exit codes)

```bash
./mvnw -Dtest=OrderServiceTest,OrderControllerTest test
./mvnw -pl :order-service -am test
./gradlew :order-service:test --tests '*.OrderServiceTest'
./gradlew :order-service:test --tests '*.OrderControllerTest'
```

Failing test → fix or explain; never delete assertions to greenwash.

## Coverage expectations for a typical feature

- Happy path service + HTTP
- Validation failure (`400`/`422`)
- Not found (`404`) when applicable
- Authz denial (`401`/`403`) when the route is protected
- Migration/schema smoke when persistence shape changed
