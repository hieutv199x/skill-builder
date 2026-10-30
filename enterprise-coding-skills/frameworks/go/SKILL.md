---
name: go-development
description: >-
  Implement and modify Go services/libraries: handlers, modules, idiomatic
  concurrency/context, and go test. Use when go.mod is present. Do not use for
  frontend UI frameworks. Prefer the repo's router and layout; don't ignore
  errors or context cancellation.
metadata:
  version: "1.1.0"
  owner: "platform-engineering"
  category: "framework-development"
  framework: "go"
---

# Go Development

## Scope

**Allowed:** packages, HTTP/gRPC handlers, services, stores, tests, small refactors tied to the task.

**Excluded:** Frontend frameworks; reckless module path renames; adding heavy frameworks when stdlib+existing router suffice.

## Detect

1. `go.mod` module path + Go version
2. Router: stdlib, chi, gin, echo, fiber, etc.
3. Layout: `cmd/`, `internal/`, `pkg/`
4. Logging/metrics already used
5. Lint: golangci-lint config
6. `AGENTS.md`

## Preconditions

- [ ] Go version known
- [ ] Handler style known
- [ ] Error wrapping style known
- [ ] Similar endpoint inspected

## Workflow

1. Analyze handler → service → storage
2. Plan files under correct `internal/` package
3. Implement with context propagation ([references/conventions.md](references/conventions.md), [references/common-tasks.md](references/common-tasks.md))
4. Verify:

```bash
go test ./internal/orders/...
golangci-lint run ./internal/orders/...
```

5. Report

## Decision rules

1. Pass `context.Context` as first param on request paths
2. Wrap errors with `%w` if that is local style
3. Table-driven tests when siblings use them

## Guardrails

- No ignored errors
- No goroutine leaks without cancellation
- No secrets in repo
- No fake test success

## References

- [references/architecture.md](references/architecture.md)
- [references/conventions.md](references/conventions.md)
- [references/common-tasks.md](references/common-tasks.md)
- [references/testing.md](references/testing.md)
- [references/anti-patterns.md](references/anti-patterns.md)

## Output Contract

Packages; Go version; tests/lint exit codes; risks.
