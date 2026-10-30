# Backfill Playbook

## Single service (default)

1. Confirm target path (`/AGENTS.md` or package root)
2. `git status` — note dirty files; don’t discard
3. Read existing `AGENTS.md` / steering / CONTRIBUTING if present
4. Inventory manifests, lockfiles, CI, entry points, contracts
5. Sample 1–3 features; classify patterns
6. Draft Identity → Architecture → Coding Rules → Workflow → Legacy → Evidence
7. Merge with previous intentional rules (see merge-existing)
8. Run quality checklist
9. Emit draft + backfill report; request owner review

## Monorepo / multi-package

1. List packages with distinct stacks (e.g. `services/api` Spring, `apps/web` Angular)
2. Backfill **one package per AGENTS.md** — don’t merge conflicting stacks into one file
3. Optional thin root `AGENTS.md` only for repo-wide git/CI rules (keep minimal)
4. Report a matrix: package → path → status (draft/missing/stale)

## Batch rollout (many services)

1. Prioritize: critical services, new services, then long-tail
2. Same template + checklist each time
3. Track: service, owner, draft PR link, approval date
4. Don’t copy AGENTS.md between services — regenerate from each repo’s evidence

## Time-box guidance

| Phase | Focus |
|---|---|
| Inventory | Manifests + CI commands |
| Sampling | Depth over breadth — 1–3 solid traces |
| Drafting | Short enforceable bullets |
| Review | Owner answers open questions |

If the repo is huge: sample + declare coverage gaps in the report — never claim exhaustive audit.
