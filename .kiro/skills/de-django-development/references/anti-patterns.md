# Django — Anti-Patterns

- N+1 queries on list endpoints
- Business logic only in templates
- `AllowAny` on write endpoints
- Huge unmanaged raw SQL without need
- Running `flush`/`migrate --fake` casually on shared envs
