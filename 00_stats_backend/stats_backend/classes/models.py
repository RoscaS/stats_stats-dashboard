from core.use.use import X
from django.db import models


class Classes(models.Model):
    date = models.DateTimeField(auto_now_add=True)

    @property
    def data(self):
        return X.getData()
