# Django — Conventions

- Model field choices/enums match local style
- DRF: ViewSet + Router when that is standard; else APIView
- Permissions: reuse `IsAuthenticated`, custom classes already in project
- Pagination/filter backends: copy neighboring viewsets
- Use `transaction.atomic` where siblings do for multi-row writes
