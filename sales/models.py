from django.db import models

# Create your models here.
class Dailysale(models.Model):
    date = models.DateField(unique=True)
    created = models.DateField(auto_now_add=True)
    updated_date =models.DateField(auto_now=True)
    total = models.FloatField()
    details = models.JSONField()
    person = models.CharField(max_length=100)
    remarks = models.CharField(max_length=200)
    cash_details = models.ForeignKey('cash.Balance',on_delete=models.CASCADE)

    def __str__(self):
        return self.date
