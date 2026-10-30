# Angular — State & HTTP

## State decision

| Existing approach | Do |
|---|---|
| Component service + RxJS | Extend that service/facade |
| NgRx store/effects | Add actions/reducers/effects in the same feature style |
| ComponentStore / signal store | Match local store helpers |
| Signals-only local UI state | Keep UI state local; don’t globalize without need |

**Never** add NgRx beside an established non-NgRx app (or vice versa) without architecture approval.

## RxJS hygiene

- Prefer `async` pipe or `takeUntilDestroyed()` over manual subscriptions
- Use existing operators (`switchMap` for search, `exhaustMap` for submits) like siblings
- Don’t nest `subscribe` inside `subscribe`

## HTTP

**Generated client present:**

```typescript
this.ordersApi.getOrder(orderId); // method must exist in generated code
```

**Hand-written services:**

```typescript
return this.http.get<OrderResponse>(`${this.base}/orders/${id}`);
```

Rules:
- Centralize base URL via existing env/config
- Reuse interceptors (auth, correlation id, error toast)
- Don’t spawn a second `HttpClient` wrapper hierarchy
- Types: reuse generated interfaces — avoid `any`

## Loading / error state

Mirror sibling UX:
- `loading` flag or dedicated state machine
- User-visible error without leaking stack traces
- Empty state for zero results
