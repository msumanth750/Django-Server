from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=64)
    approval = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Exp(models.Model):
    created_at = models.DateTimeField(auto_now_add =True)
    date = models.DateField()
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    category = models.ForeignKey('Category',on_delete = models.CASCADE)
    remarks = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name
