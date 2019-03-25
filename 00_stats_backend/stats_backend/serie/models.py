from core.use.use import x
from django.db import models


class Serie(models.Model):
    date = models.DateTimeField(auto_now_add=True)

    @property
    def data(self):
        return x.getData()
