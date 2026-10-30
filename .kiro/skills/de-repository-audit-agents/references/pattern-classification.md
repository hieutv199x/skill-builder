# Pattern Classification

Label every notable pattern before writing AGENTS.md rules.

| Label | Meaning | AGENTS.md destination |
|---|---|---|
| `GOOD` | Healthy here and compatible with stack guidance | MUST / SHOULD |
| `LEGACY-ACCEPTED` | Not ideal; intentional or constrained; still shipping | Known Exceptions / Legacy Debt |
| `BAD` | Risky, insecure, contract-hostile, or known anti-pattern | MUST NOT (+ reason) |
| `UNKNOWN` | Insufficient evidence | Gaps / open questions — **no rule** |

## Sampling guidance

- Prefer recent modules with tests over abandoned packages
- Prefer patterns that appear in ≥2 places or are enforced by lint/CI
- Prefer generated-client boundaries over hand-rolled duplicates when both exist
- One ugly file ≠ estate policy — look for recurrence and blast radius
- Security-sensitive BAD patterns can become MUST NOT from a single clear instance

## Recording format (audit notes)

```text
[path or glob] — observation — LABEL — evidence (test/CI/lint?) — AGENTS candidate
```

Example:

```text
src/.../OrderController.java — business rules in controller — BAD — no — MUST NOT: keep controllers thin
src/.../OrderService.java — @Transactional on service — GOOD — yes tests — SHOULD: TX on services
src/.../LegacyBatchJob.java — field injection — LEGACY-ACCEPTED — isolated — Exception: do not extend field injection
```

## Conflict handling

When framework guidance says GOOD but repo majority is BAD:

1. Document both in the audit report
2. MUST NOT / Legacy for the unsafe practice
3. SHOULD for the desired direction **only if** ownership agrees it is achievable
4. Never silently copy BAD into SHOULD because “everyone does it”
