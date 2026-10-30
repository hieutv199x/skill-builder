# Forms & Async UI States

## Forms

- Reactive forms when siblings use them
- Validators for UX; server remains source of truth
- Disable submit while invalid or in-flight
- Map API field errors onto controls like neighboring journeys
- Mask/format account numbers using existing helpers — don’t log raw sensitive values

## Required UI states

Every user-facing async journey change should handle:

| State | UX |
|---|---|
| Loading | spinner/skeleton per DS |
| Empty | empty state component |
| Success | confirm / navigate |
| Error | user-safe message; retry if siblings offer it |
| Forbidden | entitlement-denied experience |

## Sensitive fields

- Don’t bind secrets into `localStorage` against policy
- Avoid printing PANs/PII into analytics events
