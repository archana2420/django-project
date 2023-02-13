from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Product(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.URLField(max_length=100000,default="https://picsum.photos/200")
    description = models.CharField(max_length=150,default='This is a product')

class Order(models.Model):
    order_id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    order_date = models.DateField()
    total_purchase_amount = models.FloatField()
    address = models.TextField(blank=True,null=True)
    city = models.CharField(max_length=150,blank=True,null=True)
    state = models.CharField(max_length=150,blank=True,null=True)
    zipcode = models.CharField(max_length=10,blank=True,null=True)

class OrderDetail(models.Model):
    class Meta:
        unique_together = (('order_id','product_id'))
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.IntegerField()
    total_price = models.FloatField()
