# Angular — Architecture

Prefer the workspace layout already in use (`angular.json` / Nx).

## Common layouts

```text
# Single app
src/app/
  core/           # singleton services, auth, interceptors
  shared/         # dumb UI, pipes
  features/<name>/  # routes, pages, containers, local state
  app.routes.ts / app.config.ts

# Nx
apps/<app>/
libs/<scope>/<feature>/
libs/<scope>/data-access/
libs/<scope>/ui/
```

## Feature boundaries

| Layer | Responsibility |
|---|---|
| Route config | Lazy load, guards, titles |
| Container / page | Orchestrate data + children |
| Presentational | Inputs/outputs, rendering |
| Data-access | HTTP, facade, store |
| Core | Auth, interceptors, app-wide singles |

Rules:
- Don’t put feature HTTP calls in `AppComponent`
- Don’t import feature A deeply into feature B — use shared/data-access libs if Nx enforces boundaries
- Keep `providedIn: 'root'` only for true singletons already patterned that way
