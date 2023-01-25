from django.db import models

# Create your models here.
class Balance(models.Model):
    current_date = models.DateField(unique=True)
    created_at  = models.DateField(auto_now_add=True)
    updated_at =models.DateField(auto_now=True)
    bank = models.FloatField()
    handcash = models.FloatField()
    loose = models.FloatField()
    credits = models.FloatField()
    remarks = models.CharField(max_length=200)

    def __str__(self):
        return f'self.date self'
