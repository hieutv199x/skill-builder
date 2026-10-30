# FastAPI — Testing

```python
from fastapi.testclient import TestClient

def test_create_item(client: TestClient, auth_headers):
    r = client.post("/api/v1/items", json={"name": "x"}, headers=auth_headers)
    assert r.status_code == 201
```

- Prefer fixtures already in `conftest.py`
- Override `Depends` with `app.dependency_overrides` like sibling tests
- Async apps: use the project’s async client pattern
