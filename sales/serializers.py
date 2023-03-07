from rest_framework import serializers
from .models import Dailysale as Sale


class SaleSerializer(serializers.ModelSerializer):
    opening =serializers.SerializerMethodField()
    price =serializers.SerializerMethodField()
    receit =serializers.SerializerMethodField()
    closing =serializers.SerializerMethodField()

    class Meta:
        model = Sale
        fields = '__all__'
