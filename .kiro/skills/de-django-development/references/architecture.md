# Django — Architecture

Prefer existing app boundaries. Typical API app:

```text
apps/<feature>/
  models.py
  api/serializers.py
  api/views.py
  urls.py
  services.py          # if present
  tests/
```

Keep HTTP in views/viewsets; domain in models/services per local style.
