---
name: fastapi-development
description: >-
  Implement and modify FastAPI services: APIRouter routes, Pydantic v1/v2
  models, dependencies, auth hooks, settings, SQLAlchemy/other persistence as
  present, and pytest. Use when FastAPI is a project dependency. Do not use for
  Django-only apps or non-Python UI frameworks. Match Pydantic major to the repo.
metadata:
  version: "1.1.0"
  owner: "platform-engineering"
  category: "framework-development"
  framework: "fastapi"
---

# FastAPI Development

## Scope

**Allowed:** routers, dependencies, Pydantic schemas, service layer, persistence adapters already used, middleware/exception handlers consistent with app, pytest.

**Excluded:** Django features; adding a second web framework; inventing cloud infra unrelated to the change.

## Detect

1. `pyproject.toml` / `requirements*.txt` → `fastapi`, `pydantic`, `uvicorn`, Python `requires-python`
2. App entry: `main.py`, `app/main.py`, `create_app()` factory
3. Router layout: `include_router` prefixes/versions
4. Pydantic v1 vs v2 (`model_config` / `class Config`, `.dict()` vs `.model_dump()`)
5. DI style: `Depends()`, custom `Annotated` deps
6. DB: SQLAlchemy 1.4/2.0, SQLModel, Tortoise, raw drivers
7. Auth: OAuth2/JWT dependencies already present
8. Tests: pytest, `TestClient` / `httpx.AsyncClient`, anyio
9. `AGENTS.md` / steering

Read [references/version-compatibility.md](references/version-compatibility.md).

## Preconditions

- [ ] FastAPI + Pydantic majors known
- [ ] Sync vs async endpoint style identified
- [ ] Settings/config module identified
- [ ] Similar router inspected
- [ ] Auth dependency chain known for protected routes

## Workflow

1. **Analyze** — path, methods, schemas, status codes, side effects
2. **Plan** — router, schemas, service, repo/session, tests
3. **Implement** — thin routes; validate with Pydantic; reuse `Depends` ([references/conventions.md](references/conventions.md), [references/common-tasks.md](references/common-tasks.md))
4. **Verify**

```bash
pytest tests/api/test_items.py -q
ruff check .
mypy app || true  # only if project uses mypy
```

Use the project’s exact tooling ([references/testing.md](references/testing.md)).

5. **Report** — Output Contract

## Decision rules

1. Security/auth deps > contracts > version compatibility > healthy routers > this skill > legacy smells
2. Don’t mix Pydantic v1 and v2 APIs
3. Don’t mix sync DB calls inside async routes unless the codebase already does carefully
4. Prefer existing exception handlers / error envelopes

## Guardrails

- Never remove auth `Depends` to unblock a demo
- Never commit secrets in settings defaults
- Never log passwords/tokens
- Never claim pytest passed without running it

## References

| When | Read |
|---|---|
| Layering | [references/architecture.md](references/architecture.md) |
| Style | [references/conventions.md](references/conventions.md) |
| Recipes | [references/common-tasks.md](references/common-tasks.md) |
| Tests | [references/testing.md](references/testing.md) |
| Versions | [references/version-compatibility.md](references/version-compatibility.md) |
| Smells | [references/anti-patterns.md](references/anti-patterns.md) |

## Output Contract

Versions; routes changed; auth deps; persistence; tests + exit codes; risks.
