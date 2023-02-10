from django.db import models

# Create your models here.

class Price(models.Model):
    brand = models.ForeignKey('brands.Brand',on_delete= models.CASCADE,related_name = 'prices')
    bar_price = models.FloatField()
    mrp = models.FloatField()
    min_price = models.FloatField()
    effective_date = models.DateField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)


    def __str__(self):
        return f'{self.brand.name}({self.effective_date})'
