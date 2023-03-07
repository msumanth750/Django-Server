from rest_framework import serializers

from .models import Exp

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exp
        fields = '__all__'
