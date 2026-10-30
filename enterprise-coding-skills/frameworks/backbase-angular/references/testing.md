# Backbase Angular — Testing

## Prefer

- TestBed/Jest/Spectator as the workspace standard
- Mock facades / generated clients — don’t hit real bank APIs
- Cover entitlement-denied UI when easy to mock
- Prefer behavior tests over brittle DOM snapshots of DS internals

## Sketch

```typescript
providers: [
  { provide: TransfersFacade, useValue: facadeMock },
]
```

Assert: render, primary CTA, error banner, guard interaction if unit-testable.

## Commands

```bash
npx nx test <journey-project> --testPathPattern=transfers
npx nx lint <journey-project>
npx nx build <experience-app>
```

Record exit codes. Never fabricate PASS.
