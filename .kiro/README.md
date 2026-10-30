# Kiro workspace resources

- `skills/` — real Agent Skill directories for Kiro (copied from `../enterprise-coding-skills/...`, **not symlinks**)
- After editing source skills, regenerate with:

```bash
python3 tooling/sync-kiro-skills.py
```

Optional next steps for a consuming app repo:

1. Copy needed skills into that repo’s `.kiro/skills/`
2. Add service `AGENTS.md` via `/de-repository-audit-agents` or `/de-backfill-agents-md`
3. If required by your Kiro version, add steering or custom-agent resources that explicitly include `AGENTS.md`
