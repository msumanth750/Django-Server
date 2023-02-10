from django.urls import path

from .views import *

urlpatterns = [
    path('', stock, name="stock"),
    path('list',StocksList.as_view()),
    path('create',StockCreate.as_view(),name='Stock_create'),
    path('<pk>/',StockDetail.as_view(),name='Stock_detail'),
    path('<pk>/update',StockUpdate.as_view(),name='Stock_update'),
    path('<pk>/delete',StockDelete.as_view(),name='Stock_delete'),
    path('price/list',StockpricesList.as_view()),
    path('price/create',StockpriceCreate.as_view(),name='Stockprice_create'),
    path('price/<pk>/',StockpriceDetail.as_view(),name='Stockprice_detail'),
    path('price/<pk>/update',StockpriceUpdate.as_view(),name='Stockprice_update'),
    path('price/<pk>/delete',StockpriceDelete.as_view(),name='Stockprice_delete'),
    ]
