from django.contrib import admin

# Register your models here.
from .models import Stock,StockPrice
# Register your models here.
admin.site.register(Stock)
admin.site.register(StockPrice)
