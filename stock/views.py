from django.shortcuts import render
# Create your views here.
def stock(request):
    # brands = Brand.objects.all()
    return render(request,'stock.html')
