from django.urls import path, include
from rest_framework import routers

from .views import (BrandViewset,
                    )




router = routers.DefaultRouter()
router.register(r'', BrandViewset)

urlpatterns = [
    path('', include(router.urls)),
]
