# React — Anti-Patterns

| Smell | Do instead |
|---|---|
| Prop drilling large trees when a store/query lib exists | Use the established data/state approach |
| Fetch in `useEffect` against RSC/React Query standards | Match the repo’s data pattern |
| Broad `'use client'` on whole trees | Push client boundary down |
| Second CSS methodology | Stick to the design system |
| Disable jsx-a11y | Fix accessibility |
| Router migration inside a feature | Separate approved migration |
| Fake CI green | Run lint/test/build |
