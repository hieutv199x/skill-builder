# FastAPI — Architecture

```text
app/
  main.py              # create_app, middleware, include_router
  api/
    deps.py            # shared Depends
    v1/
      router.py
      endpoints/
  schemas/             # Pydantic models
  services/
  repositories/ or db/
  core/config.py
```

Match the repo’s names. Controllers/endpoints stay thin; services own rules; repositories own SQL.
