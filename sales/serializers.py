from rest_framework import serializers
from .models import Dailysale as Sale


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'
