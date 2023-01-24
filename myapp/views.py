from django.shortcuts import render
from django.http import HttpResponse


from brands.models import Brand

# Create your views here.
def index(request):
    # brands = Brand.objects.all()
    return render(request,'index.html')
