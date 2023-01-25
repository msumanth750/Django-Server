from django.shortcuts import render
# Create your views here.
def products(request):
    # brands = Brand.objects.all()
    return render(request,'products.html')
