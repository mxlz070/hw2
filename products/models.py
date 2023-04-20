from django.db import models


# Create your models here.
class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=250)
    description = models.TextField()
    rate = models.FloatField()
    create_date = models.DateField(auto_now=True)
    modified_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.CharField(max_length=256)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
