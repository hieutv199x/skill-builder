# Backbase Angular — Anti-Patterns

| Smell | Do instead |
|---|---|
| Inventing `@backbase/*` selectors/APIs | Verify lockfile + in-repo/typings; else UNVERIFIED stop |
| Forking DS/Backbase components | Compose + theme as estate does |
| Skipping entitlement guards | Copy sibling authz |
| Hardcoding tokens/URLs | Env/config tokens |
| One-off HttpClient vs generated clients | Shared/generated data-access |
| Second state/CSS framework | Extend current approach |
| Ignoring a11y lint | Fix markup/components |
| Logging PII in analytics | Use approved events only |
| Angular/Backbase upgrade inside feature | Separate track |
| Fake lint/test/build success | Run real commands |
| Pasting proprietary docs into skills | Keep skills process-only |
