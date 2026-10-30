# Merging with an Existing AGENTS.md

Never silently overwrite owner-approved guidance.

## Procedure

1. Read the entire existing file
2. Build a table:

| Existing rule | Still evidenced? | Action |
|---|---|---|
| … | yes / no / unknown | keep / revise / remove / ask owner |

3. **Keep** rules that remain true and intentional  
4. **Revise** rules that are directionally right but wrong on path/version/command  
5. **Remove** only with explicit note in the backfill report (and prefer asking when unsure)  
6. **Add** new rules from current audit classifications  
7. Produce a short diff summary for the owner  

## Conflict examples

| Situation | Do |
|---|---|
| Old MUST cites Boot 2 / `javax.*`; repo is Boot 3 | Revise to jakarta; cite `pom.xml` |
| Old SHOULD endorses a BAD pattern | Move to Legacy or MUST NOT; explain |
| Owner-only process rule with no code evidence | Keep if still operational; tag Evidence as “owner process” |
| Duplicate / contradictory bullets | Consolidate; ask owner if ambiguity remains |

## Draft labeling

If replacing content substantially, keep a backup suggestion:

- Commit previous file in git history (normal PR)
- Or write `AGENTS.md.draft` first when the user wants a non-destructive preview
