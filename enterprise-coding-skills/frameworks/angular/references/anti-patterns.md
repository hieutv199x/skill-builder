# Angular — Anti-Patterns

| Smell | Do instead |
|---|---|
| Subscribe without teardown | `async` pipe / `takeUntilDestroyed` |
| Nested subscriptions | Higher-order operators |
| `any` API models | Generated/interfaces |
| Logic-heavy templates | Component methods/pipes |
| New state lib beside standard | Extend current approach |
| Ignoring loading/error | Explicit UI states |
| One-off CSS duplicating design-system | Compose DS components |
| Disabling a11y lint | Fix markup |
| Assuming latest Angular syntax on old apps | Match lockfile + neighbors |
| Putting auth only in UI hide/show | Guards + server deny |
| Storing tokens in localStorage against policy | Follow existing auth storage |
| Fake green CI | Run real commands |
