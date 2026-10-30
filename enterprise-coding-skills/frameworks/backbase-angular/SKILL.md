---
name: de-backbase-angular-development
description: >-
  Implement Backbase Angular frontend journeys in depth: routing, entitlements,
  design-system composition, forms, generated API clients, state patterns already
  in use, accessibility, and UI tests. Use when @backbase/* packages are present
  or the task is a Backbase Angular journey/experience change. Do not use for
  Java backend-only tasks. Never invent Backbase component exports, selectors,
  or generated client methods — verify from lockfile and in-repo usage.
  Enterprise-proposed skill, not an official Backbase distribution.
metadata:
  version: "1.2.0"
  owner: "platform-engineering"
  category: "framework-development"
  framework: "backbase-angular"
---

# Backbase Angular Development

## Scope

**Allowed**
- Journey/feature UI in existing Backbase Angular (or Nx) apps
- Routes, lazy-loaded journeys, shells/layouts already used
- Composition of installed `@backbase/*` and design-system components **evidenced in-repo**
- Forms, validation UX, loading/empty/error states
- Wiring to generated or shared API clients already in the workspace
- Entitlement/permission guards consistent with siblings
- Unit/component tests, lint/typecheck/build for the change
- i18n keys when the app localizes journeys

**Excluded**
- Java/Spring / Backbase backend → `de-backbase-service-development`
- Pure generic Angular with no Backbase packages → `de-angular-development`
- Inventing `@backbase/*` selectors, inputs, services, or client methods
- Replacing the design system or adding a second state library without approval
- Angular/Backbase major upgrades as a feature side effect
- Hardcoding secrets, tokens, or environment URLs in the UI

**Compose with** `de-angular-development` for Angular language/framework mechanics (standalone, forms, RxJS, tests). Prefer **this** skill when journeys, entitlements, or `@backbase/*` packages are in scope.

## Detect

| # | Check | Evidence |
|---|---|---|
| 1 | Package manager / lockfile | npm / pnpm / yarn lock |
| 2 | Angular + TS + RxJS | `package.json` |
| 3 | Backbase UI packages | `@backbase/*` versions in lockfile |
| 4 | Workspace | `angular.json`, `nx.json`, app/lib graph |
| 5 | Journey layout | `journeys/`, `features/`, experience libs |
| 6 | Routing / shells | lazy routes, layout components |
| 7 | Entitlements | guards, permission directives/services already used |
| 8 | API clients | generated OpenAPI clients vs shared data-access libs |
| 9 | State | services, NgRx, facades — match area |
| 10 | Design system | internal DS + Backbase UI libs in imports |
| 11 | Tests / a11y | Jest/Karma, eslint a11y, axe if present |
| 12 | Guidance | `AGENTS.md`, steering, CONTRIBUTING |

**UNVERIFIED rule:** If a `@backbase/*` export (component, service, token) is not imported by compiling app/lib code (or typed from installed package entry points you can inspect), mark `UNVERIFIED` and **stop** — do not invent.

Read [references/version-compatibility.md](references/version-compatibility.md) and [references/backbase-ui-usage.md](references/backbase-ui-usage.md).

Inspect 1–3 sibling journeys end-to-end before copying patterns; classify GOOD / LEGACY-ACCEPTED / BAD.

## Preconditions

- [ ] Angular + each relevant `@backbase/*` version recorded
- [ ] Standalone vs NgModule style for the journey area known
- [ ] Entitlement/guard pattern identified
- [ ] API client generation / data-access boundary known
- [ ] Design-system components to reuse identified (from siblings)
- [ ] Similar journey inspected
- [ ] Test/lint commands for the project known
- [ ] Public UX impact: additive vs breaking flow

## Workflow

### 1. Analyze
Trace: journey entry → route/guards → container → DS/Backbase UI → state → API client → error/empty/loading.  
Reject smells in [references/anti-patterns.md](references/anti-patterns.md).

### 2. Plan
Minimal files:
1. Route (+ lazy) under the correct experience/journey lib
2. Container + presentational children as local style
3. Entitlement wiring
4. Form models if needed
5. Facade/client calls using **existing** methods
6. i18n keys
7. Tests

### 3. Implement
1. Routes/entitlements — [references/routing-and-entitlements.md](references/routing-and-entitlements.md)
2. Compose UI — [references/component-patterns.md](references/component-patterns.md), [references/backbase-ui-usage.md](references/backbase-ui-usage.md)
3. Data — [references/data-access.md](references/data-access.md)
4. Forms/UX — [references/forms-and-states.md](references/forms-and-states.md)
5. a11y — [references/accessibility.md](references/accessibility.md)
6. Recipes — [references/common-tasks.md](references/common-tasks.md)
7. Angular mechanics via `de-angular-development` references as needed

### 4. Verify

```bash
npx nx lint <project>
npx nx test <project> --testPathPattern=journey
npx nx build <project>
# or ng equivalents from package scripts
```

Details: [references/testing.md](references/testing.md).

### 5. Report
Output Contract — include UNVERIFIED items if any blocked the work.

## Decision rules

1. Security/entitlements > approved UX/contracts > lockfile peer deps > AGENTS.md > healthy sibling journeys > `de-angular-development` defaults > BAD legacy  
2. Installed package exports > blog posts / memory of “Backbase components”  
3. Generated/shared clients > new ad-hoc `HttpClient` services when generation is standard  
4. Don’t bypass entitlements to demo a screen  
5. Don’t upgrade `@backbase/*` or Angular inside a journey feature  

| Situation | Choose |
|---|---|
| Sibling uses a Backbase DS button/table | Compose same imports — don’t fork CSS |
| Client method missing in generated API | Update contract/generation workflow — don’t invent the method |
| Entitlement guard on sibling write flows | Copy the same guard/directive |
| Journey area is NgModule | Stay NgModule |
| Journey area is standalone | Stay standalone |
| Need a Backbase component never imported in-repo | Verify from package exports; else UNVERIFIED stop |

## Guardrails

- Never invent `@backbase/*` APIs or selectors
- Never hardcode tokens, API keys, or environment URLs in UI code
- Never skip entitlement checks on sensitive journeys
- Never disable a11y lint to land UI
- Never introduce a second state/CSS framework
- Never claim verification without execution evidence
- Never paste proprietary Backbase docs into skill files

## References

| When | Read |
|---|---|
| Journey structure | [references/architecture.md](references/architecture.md) |
| Composing Backbase/DS UI | [references/backbase-ui-usage.md](references/backbase-ui-usage.md) |
| Components / templates | [references/component-patterns.md](references/component-patterns.md) |
| Routes & entitlements | [references/routing-and-entitlements.md](references/routing-and-entitlements.md) |
| API clients / facades | [references/data-access.md](references/data-access.md) |
| Forms & async UI states | [references/forms-and-states.md](references/forms-and-states.md) |
| a11y | [references/accessibility.md](references/accessibility.md) |
| Recipes | [references/common-tasks.md](references/common-tasks.md) |
| Tests | [references/testing.md](references/testing.md) |
| Versions / peers | [references/version-compatibility.md](references/version-compatibility.md) |
| Smells | [references/anti-patterns.md](references/anti-patterns.md) |

## Verification checklist

- [ ] Entitlements/guards preserved on sensitive routes
- [ ] Only verified `@backbase/*` / DS imports used
- [ ] Loading / empty / error states present
- [ ] No secrets in frontend bundles
- [ ] a11y labels/focus for new interactive controls
- [ ] Targeted tests run (or gap documented)
- [ ] lint/test/build exit codes recorded

## Output Contract

```markdown
## Backbase Angular change report
- Angular / @backbase/* versions (evidenced):
- Journey / libs changed:
- Routes + entitlements:
- API client methods used (verified):
- Design-system / Backbase UI reuse:
- a11y notes:
- Tests + commands/exit codes:
- UNVERIFIED items:
- Approvals needed:
```
