# Backbase SDK — Compatibility Policy

**Do not invent SDK methods. Do not paste proprietary documentation here.**

## Required detection

1. Resolve Backbase BOM / product versions from Maven/Gradle
2. List direct `com.backbase.*` dependencies used by **this** module
3. Prefer APIs already referenced in compiling production/test code
4. If missing locally → `UNVERIFIED` — request licensed docs or an in-repo usage sample

## Change policy

| Change | Rule |
|---|---|
| New Backbase dependency | Rationale + BOM alignment + owner awareness |
| Public HTTP contract | Estate workflow + explicit approval if breaking |
| Generated code | Edit spec/config; regenerate; never hand-patch |
| Spring Boot upgrade with Backbase BOM | Separate compatibility review |
| Calling a new SDK method never seen in-repo | Forbidden until verified |

## Evidence hierarchy

1. Compiling in-repo usage
2. Module tests
3. Approved internal ADRs you may access
4. Licensed vendor docs (do not copy into shared skills)

Everything else is speculation.
