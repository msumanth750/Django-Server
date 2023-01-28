from rest_framework import serializers

from .models import Receit

class ReceitSerializer(serializers.ModelSerializer):
    class meta:
        model = Receit
        fields = '__all__'
