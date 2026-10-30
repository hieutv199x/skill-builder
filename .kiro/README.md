# Kiro workspace resources

- `skills/` — Agent Skills exposed to Kiro (symlinks into `../enterprise-coding-skills/...`)
- Regenerate with: `python3 tooling/sync-kiro-skills.py`

Optional next steps for a consuming app repo:

1. Copy/link needed skills into that repo’s `.kiro/skills/`
2. Add service `AGENTS.md` via `/de-repository-audit-agents`
3. If required by your Kiro version, add steering or custom-agent resources that explicitly include `AGENTS.md`
