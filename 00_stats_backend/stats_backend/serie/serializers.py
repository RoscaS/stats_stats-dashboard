from rest_framework import serializers
from serie.models import Serie

class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        # fields = '__all__'
        fields = (
            'data',
        )
