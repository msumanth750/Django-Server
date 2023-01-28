from django.shortcuts import render
from rest_framework import viewsets


from .models import Brand
from .serializers import BrandSerializer
# Create your views here.
def brands(request):
    return render(request,'brands.html')

class BrandViewset(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
