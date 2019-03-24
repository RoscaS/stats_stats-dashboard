from rest_framework import viewsets

from serie.models import Serie
from serie.serializers import SerieSerializer


class SerieViewSet(viewsets.ModelViewSet):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer
