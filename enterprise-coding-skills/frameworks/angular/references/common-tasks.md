# Angular — Common Tasks

## A. New lazy routed feature

1. Create feature folder matching standalone/NgModule style
2. Add route + lazy import
3. Apply guards like siblings
4. Container loads data; children present
5. Loading/empty/error
6. Unit tests for container logic + smoke for template bindings
7. Lint/build

## B. Reactive form submit → API

1. Build form with validators
2. On submit: mark touched, block double-submit
3. Call facade/generated API
4. Map success navigation/toast like siblings
5. Map field/API errors into form
6. Tests for invalid submit + success path

## C. List + filter + pagination

1. Reuse design-system table/list
2. Sync filters to query params if neighbors do
3. Debounce search like siblings
4. Empty/error states
5. TrackBy/track for rows

## D. Add field to existing form/API

1. Update types (generated regen if needed)
2. Add control + validation
3. Wire request/response mapping
4. Update tests
5. Note additive vs breaking API

## E. Guarded page by permission

1. Reuse entitlement/permission guard
2. Hide nav entry consistently with authorization (UX may still need server deny)
3. Test redirect/deny behavior if harness exists

## F. Interceptor change

1. Touch only if required — high blast radius
2. Mirror existing interceptor ordering
3. Add tests for header injection / error mapping
4. Don’t log tokens
