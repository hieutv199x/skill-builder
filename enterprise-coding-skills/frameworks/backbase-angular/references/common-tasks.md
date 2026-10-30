# Backbase Angular — Common Tasks

## A. New journey step / page

1. Add route under the journey lib (lazy if siblings lazy)
2. Apply entitlement guard/directive like siblings
3. Container + template composing verified DS/Backbase UI
4. Facade method calling **existing** API client method
5. Loading/empty/error
6. Unit tests for container/facade
7. Lint/build

## B. Wire form → API

1. Reactive form + validators
2. Submit → facade → generated client method (verified)
3. Map success to next step / toast
4. Map API errors to fields
5. Prevent double submit
6. Tests for invalid + success paths

## C. List with entitlements

1. Reuse DS table/list
2. Hide actions the user cannot perform **and** keep route guarded
3. Empty/error states
4. Pagination/filter patterns from siblings

## D. Add field to journey + API

1. Confirm client type/field exists (regen if estate workflow requires)
2. Form control + display formatting
3. Request mapping
4. Tests
5. Note additive vs breaking UX/API

## E. Fix entitlement-denied bug

1. Reproduce with test user lacking privilege
2. Ensure guard + UI consistent
3. Regression test if harness allows mocking entitlements
