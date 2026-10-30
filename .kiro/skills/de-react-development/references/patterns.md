# React — Patterns

## Components

- Prefer small composable components aligned with the design system
- Controlled vs uncontrolled inputs — match neighbors
- Derive UI from state; avoid duplicate sourced-of-truth

## Next.js App Router

- Default Server Components; add `'use client'` only for interactivity/browser APIs
- Fetch on the server when siblings do; cache/revalidate explicitly as the app does
- Route handlers under `app/api` only if that is the backend-for-frontend pattern

## Effects & data

- Don’t fetch in `useEffect` if the repo standard is RSC/React Query/loaders
- Keep hooks pure relative to local rules; extract shared hooks when reused 2+ times

## Styling

- One system only (Tailwind / CSS modules / stitches / etc. as already chosen)
