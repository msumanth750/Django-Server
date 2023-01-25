from django.shortcuts import render
# Create your views here.
def prices(request):
    return render(request,'prices.html')
