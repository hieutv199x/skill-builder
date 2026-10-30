---
name: secure-coding
description: >-
  Apply secure coding practices across stacks: input validation, authn/authz,
  secrets handling, injection prevention, safe logging, SSRF/path traversal
  caution, and dependency restraint. Use for auth-sensitive features and
  security review of diffs. Do not use for exploit development or extracting
  production secrets.
metadata:
  version: "1.1.0"
  owner: "platform-engineering"
  category: "foundation"
---

# Secure Coding

## Scope

**Allowed:** secure implementation guidance and security review for the active change.

**Excluded:** offensive exploit authoring; dumping production secrets; disabling security controls “temporarily”.

## Detect

1. Authn/authz mechanisms in the repo
2. Secret management approach (env, vault, K8s secrets)
3. Existing security middleware/filters/guards
4. Data classification hints in AGENTS.md

## Workflow

1. Identify trust boundaries and sensitive data
2. Preserve server-side authorization
3. Validate/sanitize inputs at boundaries
4. Keep secrets out of source, logs, client bundles
5. Prefer parameterized queries / safe APIs
6. Report residual risks honestly

## Decision rules

1. Fail closed on authz when unsure — ask
2. Security policy > feature convenience
3. Don’t log tokens, passwords, PANs, session IDs

## Guardrails

- Never weaken TLS/CSRF/auth to make demos work
- Never commit `.env` / keys
- Never claim “secure” without reviewing the trust boundary

## References

- [references/checklist.md](references/checklist.md)
- [references/threat-checklist.md](references/threat-checklist.md)

## Output Contract

Security-relevant changes; controls preserved/added; residual risks.
