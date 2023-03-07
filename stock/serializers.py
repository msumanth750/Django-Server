from rest_framework import serializers

from .models import Stock
from receits.models import Receit



class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

    
