# Backbase Angular — Version Compatibility

**Prefer lockfile versions over this file.**  
This skill never invents `@backbase/*` APIs — versions only tell you what *might* exist; in-repo imports/typings prove what you may call.

## Detect

| Item | Where |
|---|---|
| `@angular/core` (+ router/forms/common) | `package.json` / lockfile |
| Each `@backbase/*` package | lockfile + actual imports in the journey |
| Design-system packages | lockfile + shared UI libs |
| Nx | `nx.json`, `@nx/angular` |
| TypeScript / Node | `typescript`, `engines` |
| Peer warnings | install logs / `pnpm why` / npm `peerDependency` notices |

Record exact versions in the change report.

---

## Compatibility rules

1. **Peer deps win** — if an installed `@backbase/*` package peers Angular `^18` and the app is on 18, don’t use Angular 19-only APIs in that journey casually  
2. **Don’t upgrade to unlock** — needing a component from a newer Backbase major is a compatibility track, not a journey feature  
3. **Lockfile > wiki memory** — outdated internal docs lose to compiling code  
4. **Angular language features** — signals / `@if` / zoneless only when Angular version **and** journey area practice allow (see `de-angular-development` version notes)  
5. **Multiple `@backbase/*` versions** in a monorepo — change the package set used by **this** app/lib; don’t assume another experience’s versions  

---

## Safe vs unsafe changes

| Change | In a journey feature PR? |
|---|---|
| Use already-installed, verified Backbase/DS component | Yes |
| Call existing generated client method | Yes |
| Add optional UI field mapped to existing API field | Yes |
| Angular major / `ng update` | **No** |
| `@backbase/*` major/minor bump for new widgets | **No** — separate review |
| New state library (NgRx/SignalStore) beside current | **No** without approval |
| Enable zoneless / SSR flips | **No** |

---

## UNVERIFIED API handling

If you cannot prove an export exists:

1. Search workspace for the symbol  
2. Inspect installed package typings if `node_modules` is present  
3. If still unknown → mark `UNVERIFIED`, stop implementation of that piece, ask for licensed docs or a sibling usage sample  

Never unblock by guessing selectors or client method names.

---

## Quick “don’t invent” list

- Backbase selectors remembered from another bank/project  
- Client methods “that should exist” on the generated API  
- That all experiences share one `@backbase/*` version set  
- That newest Angular control flow is adopted everywhere  

**Ground truth:** sibling journey imports + lockfile + typings.
