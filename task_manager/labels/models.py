from django.db import models as m


class LabelModel(m.Model):
    name = m.CharField(max_length=32, unique=True)

    def __str__(self) -> str:
        return self.name
