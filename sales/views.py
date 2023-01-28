from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SaleSerializer

from .models import Dailysale as Sale
# Create your views here.
def sales(request):
    # brands = Brand.objects.all()
    return render(request,'sales.html')

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    lookup_field = 'id'
