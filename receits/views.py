from django.shortcuts import render

from rest_framework import viewsets
from .serializers import ReceitSerializer
from .models import Receit

# Create your views here.
def receits(request):
    # brands = Brand.objects.all()
    return render(request,'receits.html')


class ReceitViewset(viewsets.ModelViewSet):
    queryset = Receit.objects.all()
    serializer_class = ReceitSerializer
    lookup_field = 'id'
