from django.urls import path, include
from rest_framework import routers

from .views import (PriceViewset,
                    )

router = routers.DefaultRouter()
router.register(r'', PriceViewset)

urlpatterns = [
    path('', include(router.urls)),
]
