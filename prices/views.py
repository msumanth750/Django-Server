from django.shortcuts import render

from rest_framework import viewsets
from .serializers import PriceSerializer
from .models import Price
# Create your views here.
def prices(request):
    return render(request,'prices.html')

class PriceViewset(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    lookup_field ='id'
