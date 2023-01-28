from django.shortcuts import render
from rest_framework import viewsets
from .models import Stock
from .serializers import StockSerializer
# Create your views here.
def stock(request):
    # brands = Brand.objects.all()
    return render(request,'stock.html')


class StockViewset(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    lookup_field = 'id'
