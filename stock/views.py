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
from brands.models import Brand
from datetime import datetime
# Create your views here.
def stock(request):
    date = request.GET.get('date',None)
    brands =Brand.objects.order_by('numericcode').values()
    stocks =[]
    for brand in brands:
        if not date:
            date = datetime.today().date()
            print(date)
        stock = Stock.objects.filter(brand=brand['id'],date=date).first()
        if stock:
            brand['qty']=stock.quantity
        else:
            brand['qty']=0


    context = {

        'brands' : brands,
        'date':date

    }

    return render(request,'stock.html',context)


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
    success_url ='/stock'

class StocksList(ListView):
    model =Stock
    template_name = 'Stock/stock_list.html'

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
