# Routing & Entitlements

## Routes

Register journeys like siblings:
- Lazy `loadChildren` / `loadComponent`
- Shell layout parents
- Titles/breadcrumbs data if used

## Entitlements / permissions

Detect how the app enforces access:
- Route `canActivate` guards
- Permission directives on UI
- Entitlement services checking scopes/privileges

Rules:
1. **Copy** the sibling pattern for equally sensitive flows
2. Server still enforces — UI hiding is not enough
3. Never remove a guard “to see the page”
4. Denied UX should match estate (redirect, empty state, error page)

## Deep links

Preserve query params / return URLs as neighboring journeys do after login or step completion.
