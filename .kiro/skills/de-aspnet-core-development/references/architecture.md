# ASP.NET Core — Architecture

```text
src/Service.Api/          # endpoints, Program.cs
src/Service.Application/  # use cases (if present)
src/Service.Domain/
src/Service.Infrastructure/  # EF, external clients
tests/Service.Tests/
```

If the repo is a single project, keep controllers/services folders consistent with neighbors.
