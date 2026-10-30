# Using @backbase/* and Design-System UI

**Never invent component selectors, inputs, outputs, DI tokens, or services.**

## Verification procedure (required)

Before adding any Backbase UI symbol:

1. **Lockfile** — confirm `@backbase/<package>` is installed for this workspace/app  
2. **In-repo usage** — find a compiling import of the same symbol in a sibling journey/shared lib  
3. **Typings fallback** — if unused yet, inspect the package’s public entrypoint `.d.ts` in `node_modules` (when present) for the export  
4. **Match import path** — secondary entry points differ (`@backbase/foo` vs `@backbase/foo/bar`); copy neighbor style  
5. If steps 2–3 fail → **`UNVERIFIED`** — do not invent; ask for an approved sample or licensed documentation  

Document the evidence path (file that imports it, or package typings path) in the change report when the symbol is new to the journey.

## Composition guidelines

| Do | Don’t |
|---|---|
| Compose DS + verified Backbase primitives | Rebuild tables/buttons from scratch beside DS |
| Reuse shared wrapper components if the estate has them | Copy-paste vendor templates into every journey |
| Use existing theme/CSS variables | One-off global CSS overrides fighting the theme |
| Keep content projection patterns from siblings | Assume every input exists without typings |

## Theming & layout

- Follow the experience’s theme module / CSS variables / design tokens  
- Prefer layout shells already used by journeys (headers, side nav, content width)  
- Responsive behavior: match sibling breakpoints; don’t invent a new grid system  

## i18n & formatting

- User-visible strings via the app’s i18n system when present  
- Money/date/account masking via shared pipes/helpers — critical for banking UX consistency  

## Proprietary content

Do **not** paste vendor screenshots, private Storybook dumps, or proprietary API tables into enterprise skill files. Skills stay process-only; evidence lives in the customer repo and licensed docs.
