from django.urls import path,include
from rest_framework import routers
from .views import (ExpenseViewSet)

router = routers.DefaultRouter()
router.register('',ExpenseViewSet)

urlpatterns = [
    path('',include(router.urls))
]
