# Quality Gate — before owner review

## Structure
- [ ] All canonical sections present (Identity → Evidence)
- [ ] File is short enough to be useful (~80–180 lines target)
- [ ] One primary stack (or clearly separated sections if unavoidable)

## Correctness
- [ ] Versions match manifests/lockfiles
- [ ] Build/test/lint commands match scripts or CI
- [ ] Paths in Architecture/Evidence exist
- [ ] MUST/SHOULD/MUST NOT derived from classifications — not vibes
- [ ] Every MUST NOT has a reason
- [ ] Legacy items are not listed as SHOULD

## Safety
- [ ] No secrets, tokens, passwords, connection strings
- [ ] No fabricated SDK/vendor APIs
- [ ] Authz-preserving rules present when the service has protected APIs/UI

## Usability for agents
- [ ] Rules are actionable on a typical PR
- [ ] “Add a field” task would not be wrongly blocked
- [ ] “Fix a null bug” task gets useful constraints
- [ ] Recommended independent skills named (if stack known)

## Process
- [ ] Audit report produced alongside AGENTS.md
- [ ] Open questions listed for owner
- [ ] Marked as **draft** until owner approval
