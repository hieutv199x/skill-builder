# Refresh Policy

Re-run `backfill-agents-md` when:

| Trigger | Why |
|---|---|
| Major framework/SDK bump | Version-sensitive rules drift |
| New public contract style (API-first ↔ code-first) | MUST rules change |
| Module boundary / ownership change | Architecture section stale |
| Security incident or new MUST NOT | Policy update |
| Owner rejects draft sections | Corrections |
| ~6–12 months idle | Preventive freshness |

## Stale signals

- Commands in AGENTS.md fail locally/CI
- Paths 404
- Stack versions disagree with lockfile
- Legacy section empty but repo full of known debt

## What not to do on refresh

- Don’t rewrite the whole file if only versions changed — surgical edit
- Don’t drop Legacy Debt without remediation evidence
- Don’t batch-refresh dozens of services without owners
