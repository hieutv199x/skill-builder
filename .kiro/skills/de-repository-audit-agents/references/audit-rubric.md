# Evidence-based repository audit rubric

For each finding record: ID, category, classification, severity (critical/high/medium/low), evidence path and line range, expected pattern, actual pattern, framework/version, confidence (high/medium/low), impact, proposed AGENTS rule, and owner decision.

## Classifications
- GOOD: demonstrated, version-compatible, secure, and sustainable; eligible for `Do` guidance.
- BAD: verified anti-pattern or risk; eligible for `Don't` guidance with remediation recommendation.
- LEGACY-ACCEPTED: known deviation documented by owner with reason/containment; mention exception without making it normative.
- UNKNOWN: insufficient evidence, ambiguous standard, unavailable proprietary documents, or unclear framework compatibility; do not write as a mandatory rule.

## Review dimensions
- Stack and architecture: entrypoints, layering, service/package boundaries, framework versions.
- APIs and integration: REST/OpenAPI, Kafka contracts, versioning, generated clients, resiliency.
- Security and privacy: secrets, authorization, validation, logging of sensitive data.
- Reliability: errors, retries, timeouts, transactions, idempotency, concurrency.
- Maintainability: coupling, duplicated logic, dependency injection, conventions, testability.
- Verification: commands, unit/integration/contract/UI tests, lint/static analysis, CI.
- Operations: tracing, structured logging, metrics, deployment configuration.
- Frontend/mobile: accessibility, loading/error states, routing, performance, platform conventions.

## Evidence rule
A proposed mandatory instruction must be backed by: an approved architecture/source-of-truth, verified local tooling/manifest, or official version-matched framework guidance. Evidence from existing code alone establishes current behavior, not a normative rule.
