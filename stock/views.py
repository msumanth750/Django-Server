from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StockSerializer
#======================================================
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
#=============================================
from .models import Stock,Stockprice

# Create your views here.
def stock(request):
    # Stocks = Stock.objects.all()
    return render(request,'stock.html')


class StockViewset(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    lookup_field = 'id'

#==============================================================
#             Django Generic views
#==============================================================

class StockCreate(CreateView):
    model =Stock
    fields = ('__all__')

class StocksList(ListView):
    model =Stock
    template_name = 'Stock.html'

class StockDetail(DetailView):
    model =Stock

class StockUpdate(UpdateView):
    model =Stock
    fields = ('__all__')
    success_url ='/Stocks/list'

class StockDelete(DeleteView):
    model =Stock

    success_url = '/Stocks/list'

class StockpriceCreate(CreateView):
    model =Stockprice
    fields = ('__all__')

class StockpricesList(ListView):
    model =Stockprice
    template_name = 'Stockprice.html'

class StockpriceDetail(DetailView):
    model =Stockprice

class StockpriceUpdate(UpdateView):
    model =Stockprice
    fields = ('__all__')
    success_url ='/Stockprices/list'

class StockpriceDelete(DeleteView):
    model =Stockprice

    success_url = '/Stockprices/list'
#==============================================================
