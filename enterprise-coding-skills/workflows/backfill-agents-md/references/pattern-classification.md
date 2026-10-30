# Pattern Classification

| Label | Meaning | Goes into AGENTS.md |
|---|---|---|
| `GOOD` | Healthy and compatible here | MUST / SHOULD |
| `LEGACY-ACCEPTED` | Imperfect but intentional/constrained | Known Exceptions |
| `BAD` | Risky / anti-pattern | MUST NOT (+ reason) |
| `UNKNOWN` | Not enough evidence | Gaps / questions — **no rule** |

## Sampling

- Prefer recent, tested modules
- Prefer patterns repeated or enforced by lint/CI
- Prefer generated-client boundaries over ad-hoc duplicates
- One ugly file ≠ policy (unless security-critical)

## Audit note format

```text
[path] — observation — LABEL — evidence — AGENTS candidate
```

## Conflicts

Framework guidance vs repo majority:

1. Record both in the backfill report  
2. Unsafe practice → MUST NOT or Legacy  
3. Desired direction → SHOULD only if owner-aligned  
4. Never elevate BAD to SHOULD because it is common  
