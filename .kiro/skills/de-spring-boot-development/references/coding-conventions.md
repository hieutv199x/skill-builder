# Spring Boot — Coding Conventions

Match local naming if it differs. Below is the default enterprise style when the repo is inconsistent — prefer neighbors first.

## Naming

| Artifact | Common pattern |
|---|---|
| Controller | `OrderController` |
| Application service | `OrderService` / `OrderApplicationService` |
| Repository | `OrderRepository` |
| Entity | `OrderEntity` or `Order` (match repo) |
| Request DTO | `CreateOrderRequest` |
| Response DTO | `OrderResponse` |
| Mapper | `OrderMapper` |
| Exception | `OrderNotFoundException` |
| Properties | `OrderProperties` |

## Dependency injection

```java
@RestController
@RequestMapping("/api/orders")
@RequiredArgsConstructor // if Lombok is already used
public class OrderController {
  private final OrderService orderService;

  @GetMapping("/{id}")
  public OrderResponse get(@PathVariable String id) {
    return orderService.getById(id);
  }
}
```

- Constructor injection only for Spring components
- Avoid field `@Autowired` in new code
- Avoid `@Inject` unless that is the project standard
- Prefer `final` collaborators

## DTOs & validation

```java
public record CreateOrderRequest(
    @NotBlank String customerId,
    @NotEmpty List<@Valid OrderLineRequest> lines
) {}
```

```java
@PostMapping
@ResponseStatus(HttpStatus.CREATED)
public OrderResponse create(@Valid @RequestBody CreateOrderRequest request) {
  return orderService.create(request);
}
```

- Use `record` only when JDK language level allows and neighbors use records
- Otherwise immutable classes with explicit constructors/getters as local style
- Put Bean Validation annotations on DTOs, not on JPA entities, unless the project already validates entities
- Use `@Validated` on services for method-level constraints when that pattern exists

## Services & transactions

```java
@Service
@RequiredArgsConstructor
public class OrderService {
  private final OrderRepository orderRepository;
  private final OrderMapper orderMapper;

  @Transactional(readOnly = true)
  public OrderResponse getById(String id) {
    return orderRepository.findById(id)
        .map(orderMapper::toResponse)
        .orElseThrow(() -> new OrderNotFoundException(id));
  }

  @Transactional
  public OrderResponse create(CreateOrderRequest request) {
    // business rules here
    OrderEntity saved = orderRepository.save(orderMapper.toEntity(request));
    return orderMapper.toResponse(saved);
  }
}
```

- Transactional boundary on the **application service**, not the controller
- `readOnly = true` for queries when the project uses that convention
- Don’t call `@Transactional` methods on `this` inside the same class (proxy self-invocation) — extract collaborator if needed

## Mapping

- **MapStruct present** → add methods to existing mapper interfaces; keep `componentModel = "spring"` if used
- **Manual mappers** → keep package-private static/helper style consistent
- Don’t map with a brand-new library for one endpoint

## Nullability & Optionals

- Prefer `Optional` for “maybe from repository” returns when neighbors do
- Don’t use `Optional` as field/parameter type casually
- Avoid returning `null` from services when Optional/exception is the local norm

## Logging

```java
log.info("Created order {}", orderId);          // OK — identifier
log.info("Payload {}", request);                // BAD if request has PII/secrets
```

Use the existing logging facade (`Slf4j`). No `System.out`.

## Lombok

Use Lombok **only if** the module already does (`@RequiredArgsConstructor`, `@Getter`, etc.). Don’t introduce Lombok into a Lombok-free module in a feature PR.
