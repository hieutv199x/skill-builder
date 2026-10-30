# Backbase Service — Anti-Patterns

| Smell | Do instead |
|---|---|
| Guessing SDK methods/payloads | Verify in-repo or licensed docs; else UNVERIFIED stop |
| Hand-editing generated sources | Change spec/config + regen |
| Logging PII/tokens/PAN | Log identifiers only |
| Bypassing entitlements | Preserve/copy sibling authz |
| Second HTTP/SDK stack | Extend existing adapters |
| Controllers calling remote SDKs directly | Adapter layer |
| Treating another service’s unverified pattern as law | Local healthy evidence |
| Boot/BOM upgrade inside feature | Separate review |
| Fake test success | Run real commands |
| Copying proprietary docs into skills | Keep skills process-only |
