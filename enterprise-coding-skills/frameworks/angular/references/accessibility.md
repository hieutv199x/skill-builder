# Angular — Accessibility

## Minimum for every UI change

- [ ] Interactive elements reachable by keyboard
- [ ] Visible focus (don’t remove outlines without replacement)
- [ ] Form controls have labels
- [ ] Buttons/links have accessible names
- [ ] Images have `alt` (or decorative empty alt)
- [ ] Don’t rely on color alone for errors
- [ ] Dialogs/modals trap focus if the design system expects it

## Practice

- Prefer design-system primitives — they often ship a11y behavior
- Fix eslint a11y findings; don’t disable rules
- Announce async errors politely (live regions) when siblings do

## Testing a11y

If axe/jest-axe/cypress-axe exists, run it for the touched page. Otherwise manual keyboard pass + lint.
