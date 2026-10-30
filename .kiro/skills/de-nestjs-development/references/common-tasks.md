# NestJS — Common Tasks

## A. Add a REST resource (CRUD-ish)

1. Create/extend feature folder under `src/<feature>/`
2. Add DTOs with validation matching project style
3. Implement service methods; persist via existing ORM pattern
4. Add controller routes; mirror path prefix / versioning from siblings (`/api/v1/...`)
5. Register in `FeatureModule`; import module from `AppModule` (or parent)
6. Add unit tests for service; e2e for happy path + 400 validation + 401/403 if guarded
7. Add Swagger decorators iff neighboring controllers use them

## B. Protect a route with existing auth

1. Find how authenticated routes apply guards (`JwtAuthGuard`, `RolesGuard`, …)
2. Copy the **same** guard/decorator combination — don’t invent a parallel auth stack
3. Ensure e2e sends the same auth header/cookie pattern as existing tests
4. Verify unauthorized and forbidden cases

## C. Add a field to an existing API

1. Update DTO + validation
2. Update persistence model/migration/schema **using the repo’s migration workflow**
3. Update mappers/response DTOs
4. Update tests and Swagger if present
5. Call out breaking vs additive change in the report

## D. Wire a new external HTTP client

1. Prefer existing HTTP module (`HttpModule`, custom client wrapper)
2. Put base URL/timeouts in config
3. Isolate client in a provider; mock it in unit tests
4. Map upstream errors to the API’s standard error shape

## E. Background work

- Use existing queues (`Bull`, etc.) or `SchedulerRegistry` patterns if present
- Don’t introduce a new queue product for one job without approval
