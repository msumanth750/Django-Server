from django.shortcuts import render
#======================================================
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
#=============================================
from rest_framework import viewsets

from .models import Brand
from .serializers import BrandSerializer
# Create your views here.
def brands(request):
    brands = Brand.objects.select_related('prices').values('id','name',
                                                            'numericcode',
                                                            'scode',
                                                            'category__name',
                                                            'prices__id',
                                                            'prices__mrp',
                                                            'prices__bar_price',
                                                            'prices__min_price',
                                                            'prices__effective_date')
    print(brands)
    return render(request,'brands.html',{'object_list':brands})
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
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field ='id'
