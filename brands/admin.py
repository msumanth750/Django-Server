from django.contrib import admin

from .models import (BrandCategory,
                     Brand,
                     )

# Register your models here.
admin.site.register(BrandCategory)
# admin.site.register(Brand)


from import_export.admin import ImportExportModelAdmin

class BrandAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Brand,BrandAdmin)
