# Angular — Routing & Guards

## Routes

Copy sibling patterns for:
- Lazy `loadChildren` / `loadComponent`
- Path params vs query params
- Nested children under shell layouts
- `title` / breadcrumb data

```typescript
{
  path: 'orders',
  canActivate: [authGuard],
  loadComponent: () =>
    import('./orders/order-list.component').then(m => m.OrderListComponent),
}
```

(Use `loadChildren` + module if the area is NgModule-based.)

## Guards

- Reuse existing `authGuard`, `permissionGuard`, entitlement guards
- Don’t invent a parallel auth check inside components if a guard exists
- Functional guards vs class guards — match the repo

## Resolvers

Use only if the feature area already relies on resolvers; otherwise load in the container (common modern style).

## Navigation

- Prefer `RouterLink` / `Router.navigate` patterns already used
- Preserve query params when sibling flows do (`queryParamsHandling`)
- Don’t bypass guards via imperative hacks
