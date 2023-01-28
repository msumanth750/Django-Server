from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import (BrandCategory,
                     Brand,
                     )

# Register your models here.
# admin.site.register(BrandCategory)
# admin.site.register(Brand)

@admin.register(Brand)
class BrandAdmin(ImportExportModelAdmin):
    pass

@admin.register(BrandCategory)
class BrandCategoryAdmin(ImportExportModelAdmin):
    pass
