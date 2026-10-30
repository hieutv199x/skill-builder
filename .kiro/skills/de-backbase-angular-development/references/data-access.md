# Data Access & API Clients

## Prefer generated / shared clients

1. Locate OpenAPI-generated clients or `data-access` libs
2. Call **existing** methods only
3. If a method is missing:
   - Prefer updating the shared contract + regenerating clients (estate workflow)
   - Do **not** invent a client method name
   - Do **not** bypass with a one-off `HttpClient.get('/guessed-url')` when generation is standard

## Facades

If journeys use facades:
- Keep HTTP out of presentational components
- Expose view-model observables/signals consistent with siblings
- Centralize loading/error mapping in the facade

## Interceptors

Reuse auth, correlation ID, and error interceptors already provided by the experience. Don’t register duplicate interceptors in a journey lib without need.

## Environment

- Base URLs from existing env/config tokens
- Never hardcode bank hostnames or client secrets in journey code
