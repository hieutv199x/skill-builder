---
name: de-react-development
description: >-
  Implement and modify React and Next.js UI: components, hooks, routing (App
  or Pages router), data fetching (RSC, React Query, SWR, etc. as used), forms,
  and tests. Use when package.json includes react or next. Do not use for
  Angular/Backbase Angular or backend-only Spring/Nest tasks. Do not migrate
  routers or major React versions inside a normal feature.
metadata:
  version: "1.1.0"
  owner: "platform-engineering"
  category: "framework-development"
  framework: "react"
---

# React Development

## Scope

**Allowed:** React components/hooks, Next.js pages/layouts/route handlers as already patterned, client state, tests, accessibility-minded UI.

**Excluded:** Angular; inventing a new data library beside the standard; Pages↔App Router migration without approval.

## Detect

1. `react` / `next` versions from lockfile  
2. Router: Next App Router (`app/`), Pages (`pages/`), React Router, Remix-like  
3. Data: RSC/fetch, React Query, SWR, RTK Query, relay  
4. UI: existing design system, CSS modules, Tailwind, styled-components, etc.  
5. Forms: react-hook-form, Formik, uncontrolled  
6. Tests: Vitest/Jest + Testing Library, Playwright/Cypress  
7. `AGENTS.md` / steering  

## Preconditions

- [ ] React/Next versions known  
- [ ] Client vs Server Component boundary understood (Next App Router)  
- [ ] Data-fetch style identified  
- [ ] Similar feature inspected  

## Workflow

1. Analyze route → UI → data → mutations  
2. Plan minimal files; reuse design-system  
3. Implement with loading/empty/error; match server/client boundaries ([references/patterns.md](references/patterns.md), [references/common-tasks.md](references/common-tasks.md))  
4. Verify:

```bash
npm run lint
npm run test -- feature-name
npm run build
```

5. Report evidence  

## Decision rules

1. Installed APIs > “React 19 blog” advice  
2. Don’t add `'use client'` broadly — push client boundary down  
3. Don’t introduce Redux into a React Query app without approval  
4. Prefer existing form library  

## Guardrails

- No secrets in client bundles  
- No disabling eslint-plugin-jsx-a11y casually  
- No fabricated pass results  

## References

- [references/patterns.md](references/patterns.md)  
- [references/common-tasks.md](references/common-tasks.md)  
- [references/testing.md](references/testing.md)  
- [references/version-compatibility.md](references/version-compatibility.md)  
- [references/anti-patterns.md](references/anti-patterns.md)  

## Output Contract

React/Next versions; files changed; server/client notes; commands/exit codes; risks.
