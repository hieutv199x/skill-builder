# Backbase Angular — Component Patterns

## Match the journey area

- Standalone vs NgModule: copy the journey’s style
- `OnPush` if siblings use it
- Container (smart) vs presentational split only when the journey already splits

## Templates

- Prefer design-system / verified Backbase components for buttons, inputs, tables, banners
- Control flow syntax (`@if` vs `*ngIf`) — match the file/area
- Keep banking amounts/dates via existing pipes/formatters (locale, currency)
- Don’t reimplement formatters that shared libs already expose

## Journey steps

Multi-step flows (e.g. transfer/payment):
1. Copy the estate’s stepper/wizard pattern
2. Preserve draft state the way siblings do (facade/store)
3. Guard leaving dirty forms if that UX exists
4. Ensure each step respects entitlements

## Errors & messaging

Reuse toast/banner/alert components already in the experience — don’t invent a parallel notification stack.
