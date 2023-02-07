"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from myapp.views import index

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('authenticate.urls')),
    path('brands/',include('brands.urls')),
    path('stock/',include('stock.urls')),
    path('sales/',include('sales.urls')),
    path('receits/',include('receits.urls')),
    path('cash/',include('cash.urls')),
    path('products/',include('products.urls')),
    path('prices/',include('prices.urls')),
    path('',index,name='dashboard')
]+[
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/brands/',include('brands.api_urls')),
    path('api/stock/',include('stock.api_urls')),
    path('api/sales/',include('sales.api_urls')),
    path('api/receits/',include('receits.api_urls')),
    # path('api/cash/',include('cash.api_urls')),
    path('api/products/',include('products.api_urls')),
    path('api/prices/',include('prices.api_urls')),
]
