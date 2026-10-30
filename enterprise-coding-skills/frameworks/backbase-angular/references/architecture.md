# Backbase Angular — Architecture

Process-level guidance. Confirm folder names in the target workspace.

## Typical layout (Nx or Angular CLI)

```text
apps/<experience-app>/
libs/<retail|business>/<journey-name>/
  feature/          # routes, containers, journey entry
  ui/               # presentational components (if split)
  data-access/      # facades, API client wrappers
  util/             # pure helpers
libs/shared/        # design-system wrappers, auth, entitlements
```

Some estates use `journeys/<name>` inside a monolith app — match that instead of inventing Nx structure.

## Boundaries

| Layer | Responsibility |
|---|---|
| Experience app | bootstrap, shell, top-level routes |
| Journey feature | user flow pages/steps |
| Data-access | talk to generated clients / BFF |
| Shared UI | DS + verified Backbase UI wrappers |

Rules:
- Don’t dump a new journey into `AppModule` without following sibling registration
- Don’t import deep internals across journey libs against Nx boundaries
- Keep banking rules that belong on the server — UI validates UX only
