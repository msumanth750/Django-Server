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
import requests
def brands(request):
    brands=requests.get('https://fairbar.site/api/brands/').json()
    return render(request,'brands.html',{'brands':brands})
#==============================================================
#             Django Generic views
#==============================================================

class BrandCreate(CreateView):
    model =Brand
    fields = ('__all__')

class BrandsList(ListView):
    model =Brand
    template_name = 'brands.html'

class BrandDetail(DetailView):
    model =Brand

class BrandUpdate(UpdateView):
    model =Brand
    fields = ('__all__')
    success_url ='/brands/list'

class BrandDelete(DeleteView):
    model =Brand

    success_url = '/brands/list'
#==============================================================

class BrandViewset(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field ='id'
