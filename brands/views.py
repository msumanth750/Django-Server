from django.shortcuts import render

# Create your views here.
def brands(request):
    return render(request,'brands.html')
