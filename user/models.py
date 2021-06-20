from datetime import datetime

from django.db import models
from product.models import Variation
# Create your models here

class Address(models.Model):
    number = models.IntegerField(default='')
    lane = models.CharField(default='',max_length=500)
    street = models.CharField(default='',max_length=500)
    district = models.CharField(default='',max_length=500)
    city = models.CharField(default='',max_length=500)

class Fullname(models.Model):
    firstname = models.CharField(default='',max_length=500)
    midname = models.CharField(default='',max_length=500)
    lastname = models.CharField(default='',max_length=500)

class Account(models.Model):
    username = models.CharField(default='',max_length=500)
    password = models.CharField(default='',max_length=500)

class User(models.Model):
    fullname = models.ForeignKey(Fullname,on_delete=models.CASCADE , blank=True,null=True)
    address = models.ForeignKey(Address,on_delete=models.CASCADE,blank=True,null=True)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    phonenumber = models.CharField(default='',max_length=100)
    user_premission = models.CharField(default='',max_length=100)
class Comment(models.Model):
    content = models.TextField(default='',max_length=1000)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    variation = models.ForeignKey(Variation,on_delete=models.CASCADE)
    comment_date = models.DateTimeField(default=datetime.now , blank=True)
    def __str__(self):
        return f"{self.content}, {self.comment_date}"
class Love(models.Model):
    numberLove = models.IntegerField(default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    variation = models.ForeignKey(Variation,on_delete=models.CASCADE)
    love_date = models.DateTimeField(default=datetime.now , blank=True)
    def __str__(self):
        return f"{self.numberLove}, {self.variation.title}"
