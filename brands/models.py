from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)
    numericcode = models.IntegerField(unique=True)
    scode = models.CharField(max_length=150)
    category = models.ForeignKey('BrandCategory',on_delete = models.CASCADE)
    sort_order = models.IntegerField(unique=True)

    def __str__(self):
        return self.name;

class BrandCategory(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name;
