# FastAPI — Common Tasks

## Add endpoint
1. Schema request/response
2. Service method
3. Router function with Depends
4. pytest: 200/201, 422 validation, 401/403 if protected

## Add persistence field
1. Migration via Alembic/repo workflow if used
2. Update schema + repo
3. Tests for default/null behavior

## Protect route
Reuse existing `get_current_user` / role deps — do not invent parallel JWT parsing.
