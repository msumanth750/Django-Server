from django.shortcuts import render
#======================================================
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
#=============================================

from rest_framework import viewsets
from .serializers import PriceSerializer
from .models import Price
from django.urls import reverse_lazy
# Create your views here.
def prices(request):
    return render(request,'prices.html')

class PriceViewset(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    lookup_field ='id'

#==============================================================
#             Django Generic views
#==============================================================

class PriceCreate(CreateView):
    model =Price
    fields = ('__all__')
    success_url = reverse_lazy('brandlist')

class PricesList(ListView):
    model =Price
    template_name = 'prices.html'

class PriceDetail(DetailView):
    model =Price

class PriceUpdate(UpdateView):
    model =Price
    fields = ('__all__')
    # success_url ='/Prices/list'
    success_url = reverse_lazy('brandlist')

class PriceDelete(DeleteView):
    model =Price

    success_url = '/Prices/list'
#==============================================================
