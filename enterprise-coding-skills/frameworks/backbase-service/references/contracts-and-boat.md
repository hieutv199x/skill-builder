# Contracts & BOAT / OpenAPI

Process guidance for Backbase Java services that publish HTTP APIs. Confirm exact plugin goals in the target build.

## Locate the source of truth

Search in order:

1. Build plugin config (BOAT, openapi-generator, `swagger-codegen`, custom)
2. Spec paths referenced by that plugin (`openapi.yaml`, `openapi/**/*.yaml`, `specs/`)
3. README/AGENTS notes about “API first” vs “code first”
4. Generated output directories (`target/generated-sources`, `build/generated`)

If no generator exists, treat DTOs + springdoc/annotations as the contract — still report public impact.

---

## API-first happy path

```text
edit spec → run generator goal → compile → fix hand-written impl → test
```

1. **Edit the spec** intentionally (operationId, path, schemas, examples, error responses)
2. **Classify** additive vs breaking (see below)
3. **Run the repo’s exact command** (do not invent plugin names), e.g. patterns like:
   - Maven plugin goal bound to `generate-sources`
   - Explicit `./mvnw boat:...` / `openapi-generator` if documented
4. **Never hand-patch** generated Java to “make it compile”
5. Update hand-written delegates/services/mappers until the module compiles
6. Run API/contract/unit tests

---

## Additive vs breaking

| Change | Usually additive | Usually breaking |
|---|---|---|
| New optional response field | ✅ | |
| New endpoint | ✅ | |
| New optional request field | ✅ (clients may ignore) | |
| New **required** request field | | ✅ |
| Remove field/endpoint | | ✅ |
| Rename field / change type | | ✅ |
| Tighten validation rejecting old payloads | | ✅ |
| Change auth requirements more strictly | | ✅ (coordinate) |

Breaking changes need explicit owner approval and often coordinated consumer releases.

---

## BOAT / generator hygiene

- Keep generator config (mapping, package names, `modelNameMapping`) under version control as the repo already does
- Don’t change generator package names mid-feature — causes huge diffs
- If generation fails, fix the **spec** (invalid `$ref`, duplicate operationIds) first
- Review generated diff: should be limited to the intended operations

---

## Error & example alignment

- Align OpenAPI error responses with the service’s Problem Details / error envelope
- Examples should be sanitized — no real PII
- Status codes must match what the hand-written advice actually returns

---

## Code-first services

When specs are generated from code or absent:

1. Update DTOs/validation/annotations consistently with siblings
2. If a published external contract exists outside the repo, call out drift risk
3. Still fill the change report’s “public contract impact”

## Do not

- Commit only half of a regen (spec changed, sources stale)
- Divergent handwritten models that disagree with the published spec
- “Temporary” fields undocumented in the contract for mobile/web consumers
