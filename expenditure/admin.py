from django.contrib import admin

# Register your models here.
from .models import Exp,Category

admin.site.register(Exp)
admin.site.register(Category)
