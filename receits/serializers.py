from rest_framework import serializers

from .models import Receit

class ReceitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Receit
        fields = '__all__'
