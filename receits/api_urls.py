from django.urls import path,include

from rest_framework import routers

from .views import ReceitViewset

router =routers.DefaultRouter()
router.register('',ReceitViewset)

urlpatterns = [
    path('',include(router.urls))
]
