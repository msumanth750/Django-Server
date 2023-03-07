from django.shortcuts import render
from django.http import HttpResponse


from brands.models import Brand
import random
import locale
locale.setlocale(locale.LC_MONETARY, 'en_IN')

# Create your views here.
def index(request):
    # brands = Brand.objects.all()
    context ={}
    context['sales'] =locale.currency(random.randint(1000000,20000000), grouping=True)
    context['expenditure'] =locale.currency(random.randint(1000000,20000000), grouping=True)
    context['counter'] =locale.currency(random.randint(1000000,2000000), grouping=True)
    context['loans'] =locale.currency(random.randint(10000000,200000000), grouping=True)

    return render(request,'index.html',context)
