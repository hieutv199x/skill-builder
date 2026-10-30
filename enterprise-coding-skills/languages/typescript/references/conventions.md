# TypeScript Conventions

- Honor `strict` / `noImplicitAny` / `exactOptionalPropertyTypes` as configured
- Prefer `unknown` over `any` at boundaries, then narrow
- Reuse generated API types when present
- Align with ESM vs CJS and path aliases already configured
- Prefer union literals over enums if the repo does
