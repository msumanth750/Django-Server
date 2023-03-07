from django.contrib import admin

# Register your models here.
from .models import Receit,ReceitMeta

# admin.site.register(Receit)
admin.site.register(ReceitMeta)

from import_export.admin import ImportExportModelAdmin

class ReceitAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Receit,ReceitAdmin)
