# Angular — Component Patterns

## Standalone vs NgModule

Match the **feature area**. Example standalone:

```typescript
@Component({
  selector: 'app-order-list',
  standalone: true,
  imports: [CommonModule, RouterLink, DesignTable],
  templateUrl: './order-list.component.html',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class OrderListComponent { ... }
```

NgModule areas: declare in the local module; export only what other modules need.

## Change detection

- If neighbors use `OnPush`, new components should too
- Prefer immutable updates / observables with `async` pipe
- Avoid deep mutable edits that OnPush won’t see

## Templates

- Prefer control flow already used (`@if` / `@for` vs `*ngIf` / `*ngFor`)
- Use `track` / `trackBy` for lists when siblings do or lists are large
- Keep templates declarative — move non-trivial logic to TS
- Don’t call expensive methods in template bindings on every CD cycle

## Inputs / outputs

```typescript
@Input({ required: true }) orderId!: string;
@Output() readonly refresh = new EventEmitter<void>();
```

Use `input()` / `output()` signal APIs **only** if Angular version + codebase already do.

## Container vs presentational

Split only when the feature already does. Otherwise keep a pragmatic page component — don’t over-architect.

## Styling

- Reuse design-system components/tokens
- Prefer component styles / existing CSS strategy (Tailwind, CSS modules, etc.)
- Avoid `ViewEncapsulation.None` without need
- Don’t introduce a second styling framework
