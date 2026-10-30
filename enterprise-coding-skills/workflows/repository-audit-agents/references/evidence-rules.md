# Evidence Rules

Every AGENTS.md rule must be traceable.

## Accepted evidence

| Strength | Examples |
|---|---|
| High | Lockfile version; CI job command; lint config enforcing rule; test asserting behavior; OpenAPI as checked-in contract |
| Medium | Repeated pattern in ≥2 active modules; README script matching local run |
| Low | Single file; outdated wiki; comment without code |

- High → eligible for MUST  
- Medium → SHOULD or MUST NOT with care  
- Low → Legacy note or open question — not MUST  

## Forbidden “evidence”

- “Everyone knows…”
- Blog posts about the newest framework release when lockfile is older
- Patterns copied from a different service without checking this repo
- Guessed npm/Maven script names

## Citing in Evidence section

```markdown
## Evidence
- Stack: `pom.xml` (Spring Boot 3.3.x), `.java-version` 21
- Test command: `.github/workflows/ci.yml` job `test` → `./mvnw verify`
- Thin controllers: `.../api/OrderController.java`, `.../api/PaymentController.java`
- Legacy field injection: `.../batch/LegacyJob.java` (do not extend)
```

## Refresh triggers

Re-audit when:
- Major dependency bump
- Module boundary change
- New public contract style
- Owner rejects or amends rules after incidents
