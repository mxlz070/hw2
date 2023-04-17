from django.db import models


# Create your models here.
class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=250)
    description = models.TextField()
    rate = models.FloatField()
    create_date = models.DateField(auto_now=True)
    modified_date = models.DateField(auto_now_add=True)
