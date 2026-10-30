# FastAPI — Conventions

- Prefer `APIRouter(prefix=..., tags=...)` consistent with siblings
- Declare `response_model` and status codes explicitly when neighbors do
- Use `Annotated[..., Depends(...)]` if that is the local style
- Settings via pydantic-settings / existing `core/config`
- Raise `HTTPException` or domain errors already mapped by handlers
