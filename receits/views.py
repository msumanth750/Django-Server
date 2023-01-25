from django.shortcuts import render
# Create your views here.
def receits(request):
    # brands = Brand.objects.all()
    return render(request,'receits.html')
