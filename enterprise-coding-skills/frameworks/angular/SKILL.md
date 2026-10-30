---
name: angular-development
description: >-
  Implement and modify Angular applications in depth: standalone or NgModule
  components, routing/lazy loading, reactive forms, HttpClient or generated
  clients, RxJS/Signals state as already used, accessibility, Nx/workspace
  layouts, and unit/component tests. Use when package.json includes
  @angular/core. Do not use for Java backend-only tasks or Backbase-specific UI
  SDK work (use backbase-angular-development). Never assume the newest Angular
  APIs without lockfile evidence.
metadata:
  version: "1.2.0"
  owner: "platform-engineering"
  category: "framework-development"
  framework: "angular"
---

# Angular Development

## Scope

**Allowed**
- Components, templates, pipes, directives
- Routing (eager/lazy), guards, resolvers as patterned
- Reactive or template-driven forms matching neighbors
- Services, facades, existing state libraries (NgRx, Signals store, etc.)
- HTTP via generated clients or existing `HttpClient` wrappers
- Styling via the app’s design system / CSS approach
- Unit/component tests, lint/typecheck/build fixes for the change
- Nx library boundaries when the workspace uses Nx

**Excluded**
- Backend-only Java/Spring work
- Backbase `@backbase/*` journey SDK work → `backbase-angular-development`
- Replacing the design system or introducing a second state library without approval
- Angular major upgrades or NgModule→standalone migrations as a feature side effect
- Inventing APIs from a newer Angular than the lockfile

## Detect

Record **path + version evidence** before edits:

| # | Check | Where |
|---|---|---|
| 1 | Package manager | `package-lock.json` / `pnpm-lock.yaml` / `yarn.lock` |
| 2 | Angular / TS / RxJS / Node | `package.json` `dependencies` + `engines` |
| 3 | Workspace | `angular.json`, `nx.json`, `project.json`, app vs lib graph |
| 4 | Bootstrap style | Standalone `bootstrapApplication` vs `AppModule` |
| 5 | Feature style | Standalone components vs NgModules in the area you edit |
| 6 | Control flow | `@if`/`@for` vs `*ngIf`/`*ngFor` |
| 7 | Change detection | Default vs `OnPush` prevalence |
| 8 | State | services+RxJS, NgRx, ComponentStore, Signals, Akita, … |
| 9 | HTTP | generated OpenAPI client vs hand-written services |
| 10 | UI kit | Material, enterprise design-system, internal libs |
| 11 | Forms | reactive vs template-driven; typed forms if used |
| 12 | Tests | Jest vs Karma/Jasmine; TestBed / Spectator / Testing Library |
| 13 | a11y | eslint-plugin-jsx-a11y analogue / `@angular-eslint`, axe rules |
| 14 | Guidance | `AGENTS.md`, steering, CONTRIBUTING |

Read [references/version-compatibility.md](references/version-compatibility.md).

Inspect 1–3 sibling features end-to-end (route → container → presentational → service → test) and classify GOOD / LEGACY-ACCEPTED / BAD before copying.

## Preconditions

- [ ] Angular major (+ key libs) recorded from lockfile
- [ ] Standalone vs NgModule chosen to **match the feature area**
- [ ] State approach identified (do not mix)
- [ ] HTTP client approach identified
- [ ] Route/lazy-load style identified
- [ ] Design-system components identified for reuse
- [ ] Auth/guard/entitlement expectations known
- [ ] Test command for a narrow slice known
- [ ] Public UX contract impact noted (breaking copy/flow vs additive)

State assumptions explicitly when evidence is missing.

## Workflow

### 1. Analyze
Trace: route → guards → container → children → state → API → error/empty/loading.  
Reject smells in [references/anti-patterns.md](references/anti-patterns.md).

### 2. Plan
Minimal file set, typically:
1. Route config (+ lazy import)
2. Container component + template
3. Presentational children (only if local style splits them)
4. Form model / validators
5. Facade/store/service methods
6. Types (prefer generated)
7. Tests
8. i18n keys if the app localizes

### 3. Implement
Order:
1. Types/API client methods that **already exist** or are generated from updated contracts
2. State/service layer
3. Components with loading/empty/error
4. Forms — [references/forms.md](references/forms.md)
5. Routing/guards — [references/routing-and-guards.md](references/routing-and-guards.md)
6. a11y — [references/accessibility.md](references/accessibility.md)
7. Patterns — [references/component-patterns.md](references/component-patterns.md), [references/state-and-http.md](references/state-and-http.md)
8. Recipes — [references/common-tasks.md](references/common-tasks.md)

### 4. Verify

```bash
# Angular CLI
npx ng lint
npx ng test --no-watch --browsers=ChromeHeadless --include='**/feature/**/*.spec.ts'
npx ng build

# Nx
npx nx lint <project>
npx nx test <project> --testPathPattern=feature
npx nx build <project>
```

Use the package manager from the lockfile. Details: [references/testing.md](references/testing.md).

### 5. Report
Fill Output Contract with real exit codes.

## Decision rules

Priority: security/entitlements > approved UX/contracts > version compatibility > AGENTS.md > healthy neighbors > this skill > BAD legacy.

| Situation | Choose |
|---|---|
| Feature area is standalone | Stay standalone — don’t create NgModule wrappers |
| Feature area is NgModule | Stay NgModule — don’t migrate mid-bugfix |
| App uses `OnPush` | New components `OnPush` |
| NgRx is standard | Extend store — don’t add Akita/Signals store beside it |
| Signals already used in area | Match signals style; don’t force NgRx |
| Generated API client exists | Call generated methods — don’t duplicate DTO clients |
| Control flow is `@if` | Use `@if`/`@for` |
| Control flow is `*ngIf` | Keep structural directives |
| Reactive forms nearby | Reactive forms — don’t introduce template-driven casually |
| Design-system button/table exists | Compose it — don’t restyle from scratch |

## Guardrails

- Never invent Angular APIs newer than the lockfile
- Never bypass route guards / entitlement checks
- Never disable a11y lint to land UI
- Never introduce a second CSS/state framework
- Never put secrets/tokens in frontend code
- Never claim lint/tests/build passed without running them
- Keep public routes/UX changes additive unless approved

## References

| When | Read |
|---|---|
| App/lib structure | [references/architecture.md](references/architecture.md) |
| Components, templates, CD | [references/component-patterns.md](references/component-patterns.md) |
| Routes, guards, lazy | [references/routing-and-guards.md](references/routing-and-guards.md) |
| Forms & validation UX | [references/forms.md](references/forms.md) |
| RxJS, Signals, HTTP | [references/state-and-http.md](references/state-and-http.md) |
| a11y | [references/accessibility.md](references/accessibility.md) |
| Recipes | [references/common-tasks.md](references/common-tasks.md) |
| Tests | [references/testing.md](references/testing.md) |
| Version matrix | [references/version-compatibility.md](references/version-compatibility.md) |
| Smells | [references/anti-patterns.md](references/anti-patterns.md) |

## Verification checklist

- [ ] Loading / empty / error states covered in UI
- [ ] Guards/entitlements preserved
- [ ] Forms validate and surface API errors like siblings
- [ ] a11y: labels, focus, keyboard for custom controls
- [ ] Targeted unit/component tests added or gap documented
- [ ] lint / test / build commands executed with exit codes

## Output Contract

```markdown
## Angular change report
- Angular / TS / RxJS (evidenced):
- Standalone | NgModule (feature area):
- State / HTTP approach:
- Routes / components changed:
- Design-system reuse:
- a11y notes:
- Tests added/updated:
- Commands + exit codes:
- Skipped checks + reason:
- Assumptions / approvals needed:
```
