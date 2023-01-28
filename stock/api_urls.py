from django.urls import path, include
from rest_framework import routers

from .views import (StockViewset,
                    )

router = routers.DefaultRouter()
router.register(r'',StockViewset)

urlpatterns = [
    path('',include(router.urls))
]
