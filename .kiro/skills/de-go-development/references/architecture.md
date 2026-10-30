# Go — Architecture

```text
cmd/<service>/main.go
internal/<feature>/
  handler.go
  service.go
  store.go
```

Keep `internal/` private. Public `pkg/` only if the repo already publishes packages.
