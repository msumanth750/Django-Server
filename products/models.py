from django.db import models
from brands.models import (Brand,
                            )

# Create your models here.
class ProductCategory(models.Model):
    name =models.CharField(max_length=100,unique=True)
    code = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name;

class Product(models.Model):
    name = models.CharField(max_length=150,unique=True)
    code = models.CharField(max_length=150,unique=True)
    brand = models.ForeignKey('brands.Brand',on_delete=models.CASCADE)
    category = models.ForeignKey('ProductCategory',on_delete=models.CASCADE)

    def __str__(self):
        return self.name;
