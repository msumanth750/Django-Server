from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SaleSerializer
from brands.models import Brand
from myapp.utils import current_date,get_nextdate

from brands.utils import *
from datetime import datetime

from .models import Dailysale as Sale
import requests
from mysite.settings import ApiBaseurl
# Create your views here.
def sales(request):
    base_url = ApiBaseurl
    sales = requests.get(base_url+'sales',)
    return render(request,'sales.html',{'sales':sales.json()})

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    lookup_field = 'id'
