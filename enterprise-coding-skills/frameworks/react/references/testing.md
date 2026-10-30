# React — Testing

- Prefer Testing Library queries (`getByRole`, `getByLabelText`)
- Mock network via MSW or existing test utils — match repo
- For Next, don’t over-test framework plumbing; test feature behavior
- Playwright/Cypress only when the task needs e2e and harness exists

```bash
npx vitest run src/features/orders
npx jest --testPathPattern=orders
```
