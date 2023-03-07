from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ReceitMeta(models.Model):
    invoice_number = models.CharField(max_length=150,unique=True)
    dd_amount = models.FloatField()
    invoice_amount = models.FloatField()
    given_by = models.CharField(max_length=100)
    took_by = models.CharField(max_length=100)
    extra_data = models.JSONField()

    def __str__(self):
        return self.invoice_number


class Receit(models.Model):
    brand = models.ForeignKey('brands.Brand',on_delete = models.CASCADE,related_name='receits')
    quantity = models.IntegerField()
    date = models.DateField()
    updated_date =models.DateField(auto_now=True)
    invoice = models.ForeignKey('ReceitMeta',on_delete =models.CASCADE)

    def __str__(self):
        return f'{self.brand.scode}-{self.date}'
