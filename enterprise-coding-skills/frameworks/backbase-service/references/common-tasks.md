# Backbase Service — Common Tasks

## A. Contract-first new operation

1. Add operation + schemas to OpenAPI
2. Run BOAT/generator goal from the build
3. Implement hand-written delegate/service
4. Wire adapter if downstream needed
5. Authz annotations like siblings
6. Tests: API slice + service + adapter mock
7. Report additive/breaking + regen command

## B. Extend existing operation (new field)

1. Spec field (nullable/default for compatibility)
2. Regen
3. Mapper + persistence if stored
4. Adapter mapping if sent/received upstream
5. Tests for presence/absence
6. Confirm not breaking for old clients

## C. New outbound call to existing product

1. Find existing adapter for that product
2. Add method using **verified** SDK/HTTP API
3. Error mapping + timeouts
4. Unit tests with mocks
5. If SDK method never used in-repo → UNVERIFIED stop

## D. Entitlement on write API

1. Copy sibling write entitlement
2. Security tests 401/403
3. No permitAll shortcuts

## E. Defect in adapter mapping

1. Failing test with realistic payload fixture (sanitized)
2. Minimal mapping fix
3. No drive-by refactors across generated code
