# React — Common Tasks

## New page / route

**Next App Router:** add `page.tsx` / `layout.tsx` under `app/`; keep data fetch in server components when that is the norm.  
**Pages Router:** add file under `pages/`; use `getServerSideProps`/`getStaticProps` only if siblings do.  
**SPA React Router:** add route object + element; lazy load if neighbors lazy-load.

## Data mutation

1. Use existing mutation helper (React Query `useMutation`, server action, route handler)
2. Invalidate/revalidate the same way sibling features do
3. Surface error toasts/inline errors consistently

## Form

1. Match react-hook-form / Formik / local controlled inputs
2. Schema validation (zod/yup) only if already used
3. Pending/disabled submit state

## Shared component

1. Put it where shared UI already lives
2. Prefer composition over prop explosion
3. Add Testing Library tests for behavior
