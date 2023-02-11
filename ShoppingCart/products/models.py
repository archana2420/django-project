from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.URLField(max_length=100000,default="https://picsum.photos/200")
