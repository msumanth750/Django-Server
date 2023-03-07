from django.contrib import admin

# Register your models here.
from .models import Stock,Stockprice
# Register your models here.
# admin.site.register(Stock)
admin.site.register(Stockprice)

from import_export.admin import ImportExportModelAdmin

class StockAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Stock,StockAdmin)
