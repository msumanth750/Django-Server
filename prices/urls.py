from django.urls import path
from .views import *

urlpatterns = [
    # path('', prices, name="prices"),
    path('',PricesList.as_view(),name='prices'),
   path('create',PriceCreate.as_view(),name='Price_create'),
   path('<pk>/',PriceDetail.as_view(),name='Price_detail'),
   path('<pk>/update',PriceUpdate.as_view(),name='Price_update'),
   path('<pk>/delete',PriceDelete.as_view(),name='Price_delete'),
    ]
