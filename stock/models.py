from django.db import models

# Create your models here.
class Stockprice(models.Model):
    brand = models.ForeignKey('brands.Brand',on_delete = models.CASCADE)
    date = models.DateField(auto_now_add=True)
    updated_date =models.DateField(auto_now=True)
    mrp = models.FloatField()
    bar_price = models.FloatField()
    max_price = models.FloatField()
    min_price = models.FloatField()
    discount = models.IntegerField()

    def __str__(self):
        return f'self.date self.brand'

class Stock(models.Model):
    brand = models.ForeignKey('brands.Brand',on_delete = models.CASCADE,related_name='stocks')
    quantity = models.IntegerField()
    date = models.DateField()
    updated_date =models.DateField(auto_now=True)
    # current_prices =models.ForeignKey('Stockprice',on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.brand.name} {self.date}'
