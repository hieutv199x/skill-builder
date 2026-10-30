# FastAPI — Version Compatibility

| Topic | Rule |
|---|---|
| Pydantic v2 | `model_dump`, `model_config = ConfigDict(...)` |
| Pydantic v1 | `.dict()`, `class Config` — only if installed |
| FastAPI lifespan | Prefer lifespan context if app already migrated from startup/shutdown events |
| SQLAlchemy 2.0 style | Match existing session/query style |
