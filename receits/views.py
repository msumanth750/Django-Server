from django.shortcuts import render

from rest_framework import viewsets
from .serializers import ReceitSerializer
from .models import Receit

import requests
from mysite.settings import *
# Create your views here.
def receits(request):
    base_url =ApiBaseurl
    receits =requests.get(base_url+'receits/')
    return render(request,'receits.html',{'receits':receits.json()})


class ReceitViewset(viewsets.ModelViewSet):
    queryset = Receit.objects.all()
    serializer_class = ReceitSerializer
    lookup_field = 'id'
