# Backfill Quality Checklist

Before requesting owner review:

## Structure
- [ ] Canonical sections present
- [ ] Roughly 80–180 lines (or justified longer)
- [ ] Single primary stack (or split packages)

## Correctness
- [ ] Versions match manifests/lockfiles
- [ ] Build/test/lint commands match scripts or CI
- [ ] Paths exist
- [ ] MUST/SHOULD/MUST NOT tied to classifications
- [ ] Every MUST NOT has a reason
- [ ] Legacy not listed as SHOULD

## Merge safety
- [ ] Existing AGENTS.md read (if any)
- [ ] Kept / revised / removed rules summarized
- [ ] No silent deletion of owner process rules

## Safety
- [ ] No secrets / tokens / connection strings
- [ ] No fabricated vendor APIs
- [ ] Authz-preserving guidance when applicable

## Agent usability
- [ ] “Add a field” not wrongly blocked
- [ ] “Fix a bug” gets useful constraints
- [ ] Independent skill names listed when known

## Handoff
- [ ] Marked draft pending review
- [ ] Open questions listed
- [ ] Last audited date set
