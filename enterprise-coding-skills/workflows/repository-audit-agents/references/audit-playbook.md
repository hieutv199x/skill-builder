# Audit Playbook

Execute in order. Record evidence paths as you go.

## Phase A — Surface scan (15–30 min equivalent)

1. Root listing: build files, lockfiles, CI (`.github/workflows`, GitLab CI, Jenkinsfile)
2. README / CONTRIBUTING / existing AGENTS / `.cursor/rules` / `.kiro/steering`
3. Detect monorepo vs single service; list packages to include/exclude
4. Run optional `detect-stack.py <root>` if available
5. Fill Identity draft (name, stack, commands) with confidence tags

## Phase B — Structure map

1. Source roots and test roots
2. Entry points (boot class, `main.ts`, routers)
3. Public contracts and generation config
4. Auth/security configuration locations
5. Shared libraries vs service-local code

Produce a one-screen architecture bullet list for AGENTS.md.

## Phase C — Pattern sampling

For each of 1–3 features:

1. Pick a user-visible or API-visible capability with tests if possible
2. Trace: HTTP/UI → application → persistence/adapter
3. Note: DI style, error model, validation, naming, transactions, state, client generation
4. Label each note `GOOD` | `LEGACY-ACCEPTED` | `BAD` | `UNKNOWN`
5. Prefer recurrence over one-off oddities

## Phase D — Cross-check

1. Compare samples to each other — is there a dominant style?
2. Flag conflicts (two error formats, two ORMs, mixed javax/jakarta)
3. Check CI: which checks are actually required on PRs?
4. Security quick pass: secrets in repo? `permitAll` on writes? tokens in frontend?

## Phase E — Author & gate

1. Draft AGENTS.md from classifications only
2. Mentally apply rules to two tasks: “add field” and “fix null bug” — do rules help or block wrongly?
3. Run quality-gate checklist
4. Write audit report + owner questions

## Monorepo tip

Audit **one package** end-to-end per AGENTS.md. A single root AGENTS.md that mixes Angular + Spring rules becomes noise — split by service.
