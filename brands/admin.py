from django.contrib import admin
from .models import (BrandCategory,
                     Brand,
                     )

# Register your models here.
admin.site.register(BrandCategory)
admin.site.register(Brand)
