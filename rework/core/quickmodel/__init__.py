"""Quick model

Quick model is inspired by SQLModel and PonyORM
issue: https://github.com/rework-union/django-rework/issues/46

Usage:

```python
from rework.core import quickmodel as QM
class Entity(QM.Model):
    name = QM.Str()
```
"""

from django.db import models
from django.db.models import Model  # noqa


class Str(models.TextField):
    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 150
        kwargs["default"] = ""
        super().__init__(*args, **kwargs)


class LongStr(models.TextField):
    def __init__(self, *args, **kwargs):
        kwargs["default"] = ""
        super().__init__(*args, **kwargs)


class Int(models.IntegerField):
    pass


class Float(models.FloatField):
    pass


class Decimal(models.DecimalField):
    def __init__(self, *args, **kwargs):
        kwargs["max_digits"] = 10
        kwargs["decimal_places"] = 2
        super().__init__(*args, **kwargs)


class Bool(models.BooleanField):
    pass


class DateTime(models.DateTimeField):
    pass


class Date(models.DateField):
    pass


class Time(models.TimeField):
    pass


class UUID(models.UUIDField):
    pass


class JSON(models.JSONField):
    pass
