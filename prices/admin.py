from django.contrib import admin

from .models import Price

# Register your models here.
# admin.site.register(Price)

from import_export.admin import ImportExportModelAdmin

class PriceAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Price,PriceAdmin)
