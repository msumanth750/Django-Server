from django.shortcuts import render
#======================================================
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
#=============================================
from rest_framework import viewsets
from myapp.utils import current_date,current_month_dates
from .models import Brand
from .serializers import BrandSerializer
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from .utils import *
from mysite.settings import *
import requests
# Create your views here.
def brands(request):
    base_url=ApiBaseurl
    sdate = request.GET.get('sdate',current_month_dates()[0].strftime("%Y-%m-%d"))
    edate = request.GET.get('edate',current_month_dates()[1].strftime("%Y-%m-%d"))

    search = request.GET.get('search',None)
    params ={}
    if search:
        params['search']=search
    if sdate and edate:
        params['sdate']=sdate
        params['edate']=edate
    brands = requests.get(base_url+'brands',params=params)
    return render(request,'brands.html',{'brands':brands.json(),
                                         'Search':search,
                                         'start':sdate,
                                         'end':edate,
                                         })
#==============================================================
#             Django Generic views
#==============================================================

class BrandCreate(CreateView):
    model =Brand
    fields = ('__all__')

class BrandsList(ListView):
    model =Brand
    template_name = 'brands/brand_list.html'

class BrandDetail(DetailView):
    model =Brand

class BrandUpdate(UpdateView):
    model =Brand
    fields = ('__all__')
    success_url ='/brands'

class BrandDelete(DeleteView):
    model =Brand

    success_url = '/brands'
#==============================================================

class BrandViewset(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field ='id'
    search_fields = ('scode','id','category__name','name')
    #
    # def get_queryset(self,request):
    #     self.request.query
