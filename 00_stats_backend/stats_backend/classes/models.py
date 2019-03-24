from core.ClassList import _ClassList
from core.settings import serie_from_excel

from django.db import models


serie = serie_from_excel('coliformes')
serie_object = _ClassList(serie, 7, 100)



class Classes(models.Model):
    date = models.DateTimeField(auto_now_add=True)

    @property
    def data(self):
        return serie_object.getData()
