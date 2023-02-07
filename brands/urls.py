from django.urls import path
from .views import *


urlpatterns =[
    path('',BrandsList.as_view()),
   path('list',brands,name='brands'),
   path('create',BrandCreate.as_view(),name='brand_create'),
   path('<pk>/',BrandDetail.as_view(),name='brand_detail'),
   path('<pk>/update',BrandUpdate.as_view(),name='brand_update'),
   path('<pk>/delete',BrandDelete.as_view(),name='brand_delete'),

]
