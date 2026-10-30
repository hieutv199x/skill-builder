# Angular — Testing

## Detect

Jest vs Karma/Jasmine; TestBed vs Spectator vs Testing Library; MSW vs `HttpTestingController`.

## Component test sketch (TestBed + standalone)

```typescript
await TestBed.configureTestingModule({
  imports: [OrderListComponent],
  providers: [{ provide: OrdersFacade, useValue: facadeMock }],
}).compileComponents();

const fixture = TestBed.createComponent(OrderListComponent);
fixture.detectChanges();
expect(fixture.nativeElement.textContent).toContain('Orders');
```

## HTTP

```typescript
const http = TestBed.inject(HttpTestingController);
facade.load('1').subscribe();
const req = http.expectOne('/api/orders/1');
expect(req.request.method).toBe('GET');
req.flush({ id: '1' });
http.verify();
```

## What to cover

- Render + primary interaction
- Loading/error presentation when non-trivial
- Form validation failing / passing
- Guard behavior if easily unit-tested

## Commands

```bash
npx ng test --no-watch --browsers=ChromeHeadless --include='**/orders/**/*.spec.ts'
npx nx test orders-feature --testPathPattern=orders
```

Prefer the project’s exact config (Jest preset, etc.). Never fake PASS.
