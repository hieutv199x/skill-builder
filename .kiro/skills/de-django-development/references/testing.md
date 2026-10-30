# Django — Testing

```bash
pytest apps/orders/tests -q
python manage.py test apps.orders
```

Use factories/fixtures already in the project (factory_boy, baker). Assert query counts only when the suite already cares.
