# Angular — Version Compatibility

**Always prefer versions from the target lockfile over this file.**  
Use this matrix to avoid inventing APIs from the wrong Angular generation.

## Detect exact versions

```bash
# from package.json / lockfile
@angular/core
@angular/router
@angular/forms
@angular/common/http
rxjs
typescript
zone.js
# workspace
@nx/angular (if present)
```

Also read `tsconfig*.json` (`strict`, `paths`) and `engines.node`.

---

## Major lines

| Angular | Typical traits | Implementer rules |
|---|---|---|
| **19+** | Signals mature; follow **installed** docs | Use `input()`/`output()` only if neighbors do |
| **17–18** | Standalone default for new apps; built-in control flow | Prefer `@if`/`@for` when the file already migrated |
| **15–16** | Standalone available; many mixed codebases | Match **feature area** style; don’t migrate casually |
| **14 and older** | NgModule-centric common | Stay NgModule unless task is an approved migration |

---

## Feature API caution

### Components & templates

| Topic | Guidance |
|---|---|
| Standalone `imports: []` | Required for standalone components — copy sibling imports |
| NgModule `declarations` | Don’t declare a standalone component in a module |
| Control flow `@if`/`@for`/`@switch` | Angular 17+ **and** local adoption |
| Legacy `*ngIf`/`*ngFor`/`ngSwitch` | Keep when the template still uses them |
| `NgOptimizedImage` | Only if already used / image CDN patterns exist |
| Deferrable views `@defer` | Don’t introduce for micro-gains without local precedent |
| Host bindings | Prefer `host:` in `@Component` when neighbors moved off `@HostBinding` |

### Signals & reactivity

| Topic | Guidance |
|---|---|
| `signal` / `computed` / `effect` | OK when area already uses signals |
| `toSignal` / `toObservable` | Use only with existing RxJS interop patterns |
| Signal inputs `input()` | Don’t rewrite `@Input()` across a feature casually |
| Zoneless change detection | **Project decision** — never enable in a feature PR |

### Forms

| Topic | Guidance |
|---|---|
| Untyped `FormGroup` | Common on older apps |
| Typed forms | Angular 14+; use when the codebase already types forms |
| `nonNullable` | Prefer when siblings use `NonNullableFormBuilder` |

### Routing

| Topic | Guidance |
|---|---|
| Functional guards | Modern style — match repo |
| Class guards `CanActivate` | Still fine if that’s the standard |
| `loadComponent` | Standalone lazy routes |
| `loadChildren` + module | NgModule lazy routes |
| `withComponentInputBinding` | Only if router already configured for it |

### HTTP & DI

| Topic | Guidance |
|---|---|
| `provideHttpClient()` | Application config / standalone bootstrap |
| `HttpClientModule` | Legacy module bootstrap — don’t mix styles randomly |
| `providedIn: 'root'` | Singletons only |
| `inject()` function | Prefer when neighbors use it over constructor DI |

### Testing

| Topic | Guidance |
|---|---|
| Karma/Jasmine | Older angular.json defaults |
| Jest / Vitest via Nx | Common in monorepos — use project executor |
| `provideHttpClientTesting()` | Newer testing setup — copy sibling specs |

---

## RxJS / TypeScript / Node

- Don’t use RxJS 7-only patterns on RxJS 6 (and vice versa) — check lockfile
- TypeScript syntax must fit the workspace `typescript` version
- Respect `engines.node` for local CLI/build

---

## Dependencies & upgrades

| Change | In a feature PR? |
|---|---|
| Feature code on current Angular | Yes |
| Adding a design-system component already depended on | Yes |
| New state library (NgRx/Akita/SignalStore) | No without approval |
| `ng update` major / migrations | **No** — dedicated upgrade track |
| Enabling zoneless / SSR flips | **No** — dedicated track |

---

## Quick “don’t invent” list

Unless lockfile + neighbors prove otherwise, do **not** assume:

- Signal-based forms as default  
- Zoneless runtime  
- `@defer` as standard list virtualization  
- That every module was migrated to standalone  
- That Jest is available when Karma is configured  

**Ground truth:** open a sibling feature and copy its imports and bootstrap style.
