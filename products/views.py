from django.shortcuts import render

from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Product

# Create your views here.
def products(request):
    return render(request,'products.html')

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field ='id'
