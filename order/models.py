from datetime import datetime

from django.db import models
from user.models import User
from product.models import Product,Variation
# Create your models here.

class Cart(models.Model):
    update_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


class Shipment(models.Model):
    address = models.CharField(default='',max_length=1000)
    price = models.IntegerField(default='')
class Payment(models.Model):
    type=models.CharField(default='',max_length=500)
    total_price = models.IntegerField(default='')
    shipment = models.ForeignKey(Shipment,on_delete=models.CASCADE,default='')
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,default='')
class Order(models.Model):
    order_description = models.TextField(default='')
    ischeck = models.BooleanField(default=False)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE)
    shipment = models.ForeignKey(Shipment,on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=datetime.now , blank=True)

class CartItem(models.Model):
    quantity = models.IntegerField(default=0)
    isorder = models.BooleanField(default=False)
    variation = models.ForeignKey(Variation,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)