# FastAPI — Anti-Patterns

| Smell | Do instead |
|---|---|
| Fat route with SQL + business rules | Service + repository |
| Unvalidated `dict` bodies | Pydantic models |
| New ORM beside standard | Extend current persistence |
| Bare except / return 200 on failure | Proper status + handlers |
| Hardcoded DB URLs | Settings / env |
| Fake test success | Run pytest |
