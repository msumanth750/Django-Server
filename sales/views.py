from django.shortcuts import render
# Create your views here.
def sales(request):
    # brands = Brand.objects.all()
    return render(request,'sales.html')
