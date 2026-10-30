---
name: django-development
description: >-
  Implement and modify Django / Django REST Framework apps: models, migrations,
  views/viewsets, serializers, permissions, admin, and tests. Use when Django is
  installed. Do not use for FastAPI-only services. Treat data migrations as
  high-risk; never run destructive commands against shared production-like DBs.
metadata:
  version: "1.1.0"
  owner: "platform-engineering"
  category: "framework-development"
  framework: "django"
---

# Django Development

## Scope

**Allowed:** models, migrations (careful), ORM queries, views/viewsets, serializers/forms, permissions, signals only if patterned, tests, admin registrations consistent with app.

**Excluded:** FastAPI; irreversible prod data ops; swapping DRF for GraphQL mid-feature without approval.

## Detect

1. Django/DRF versions; `manage.py`; settings modules
2. Apps layout; existing API style (DRF viewsets vs Django CBVs/FBVs)
3. Auth/permission classes; throttling
4. Migration history; multi-db routers if any
5. Test runner: pytest-django vs `manage.py test`
6. `AGENTS.md`

## Preconditions

- [ ] Django version known
- [ ] DRF vs non-DRF confirmed
- [ ] Migration workflow known
- [ ] Permission pattern known

## Workflow

1. Analyze model/API impact
2. Plan model → migration → serializer/view → permissions → tests
3. Implement per [references/conventions.md](references/conventions.md), [references/common-tasks.md](references/common-tasks.md)
4. Verify with project commands ([references/testing.md](references/testing.md))
5. Report including migration risk

## Decision rules

1. Prefer `select_related`/`prefetch_related` patterns from sibling code for list endpoints
2. Don’t invent permission shortcuts (`AllowAny` on sensitive views)
3. Don’t hand-write migrations that fight `makemigrations` unless repo requires it

## Guardrails

- No secrets in settings committed
- No destructive migrate on shared DBs
- No fabricated test results

## References

- [references/architecture.md](references/architecture.md)
- [references/conventions.md](references/conventions.md)
- [references/common-tasks.md](references/common-tasks.md)
- [references/testing.md](references/testing.md)
- [references/anti-patterns.md](references/anti-patterns.md)

## Output Contract

Apps/files; migrations; permissions; tests/exit codes; data risks.
