from django.shortcuts import render
from .models  import Exp

from rest_framework import viewsets
from .serializers import ExpenseSerializer

from mysite.settings import ApiBaseurl
import requests

# Create your views here.
def expenses(request):
    base_url = ApiBaseurl
    expenses = requests.get(base_url+'expenses/')

    return render(request,'exp.html',{'expenses':expenses.json()})


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Exp.objects.all()
    serializer_class = ExpenseSerializer
    lookup_field = 'id'
