# Activation and outcome cases

- Positive: "Audit this Spring Boot repo and generate AGENTS.md" -> activate.
- Positive: "Backfill coding rules for 50 Angular repos; list bad patterns" -> activate.
- Positive: "Review existing AGENTS.md against current codebase" -> activate.
- Negative: "Implement a new Spring endpoint" -> do not activate unless user also requests rules audit.
- Negative: "Fix a React component bug" -> do not activate.

## Acceptance
- Uses actual repo evidence, not invented conventions.
- Distinguishes GOOD/BAD/LEGACY-ACCEPTED/UNKNOWN.
- Has a safe draft AGENTS.md and audit report.
- Doesn't modify application code.
- Existing AGENTS.md isn't silently replaced.
- Reports unsupported framework/SDK claims as unverified.
