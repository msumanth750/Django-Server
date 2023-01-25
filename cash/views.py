from django.shortcuts import render
# Create your views here.
def cash(request):
    # brands = Brand.objects.all()
    return render(request,'cash.html')
