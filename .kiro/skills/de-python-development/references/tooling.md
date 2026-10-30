# Python Tooling

```bash
pytest tests/unit/test_foo.py -q
ruff check .
ruff format --check .
mypy src   # if configured
```

Honor poetry/uv/pip-tools — don’t switch managers mid-task.
