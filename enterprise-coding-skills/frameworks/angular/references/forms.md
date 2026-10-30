# Angular — Forms

## Choose the style already nearby

| Style | When |
|---|---|
| Reactive forms | Default in most enterprise apps |
| Typed reactive forms | When Angular version + code already use them |
| Template-driven | Only if that feature area already does |
| Dynamic form kit (Formly, etc.) | Only if already a dependency |

Don’t mix reactive and template-driven in the same feature without a strong local precedent.

---

## Reactive forms — patterns

```typescript
this.form = this.fb.nonNullable.group({
  amount: [0, [Validators.required, Validators.min(0.01)]],
  currency: ['USD', Validators.required],
  note: [''], // optional
});
```

### Submit flow (match siblings)

1. On submit: `markAllAsTouched()` (or local equivalent)
2. If `invalid`, stop — show field errors
3. Set `submitting` / disable the CTA to prevent double-post
4. Call facade/API
5. On success: navigate/toast/reset as neighbors do
6. On failure: map API errors to controls or a form-level error region

### Cross-field validation

Prefer the same approach as siblings:

- Group-level validators on `FormGroup`
- Or explicit checks in submit handler if that’s the local style

### Async validation

Use sparingly; copy debounce/`switchMap` patterns from existing async validators. Cancel stale requests.

---

## Typed forms

If the codebase uses typed `FormGroup<{ ... }>` / `NonNullableFormBuilder`:

- Keep new forms typed
- Avoid `as FormGroup` casts to escape the type system

If the codebase is untyped, don’t introduce a one-off typed form that fights local helpers.

---

## UX & accessibility

- Every control has a visible label or acceptable `aria-label`
- Error messages associated with the control (`aria-describedby` when DS supports it)
- Don’t rely on color alone for invalid state
- Preserve tab order; don’t remove focus outlines
- Disable submit while `invalid` **or** in-flight

---

## Wiring to API models

- Prefer generated request types
- Map form value → DTO in one place (component or facade) consistently
- Don’t send UI-only fields to the API without stripping
- For PATCH, distinguish “omitted” vs “null” if the API does

---

## Testing forms

- Invalid submit does not call API
- Valid submit calls API once
- API field error appears on the expected control (when applicable)
- Double-click submit doesn’t fire two mutations (if preventable)
