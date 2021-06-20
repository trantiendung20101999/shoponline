from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(default='',max_length=1000)
    description = models.CharField(default='',max_length=1000)

class Branch(models.Model):
    name = models.CharField(default='',max_length=100)
    note = models.CharField(default='',max_length=100)
class Publisher(models.Model):
    name = models.CharField(default='',max_length=100)
    address = models.CharField(default='',max_length=100)
class Author(models.Model):
    name = models.CharField(default='',max_length=100)
    dob = models.CharField(default='',max_length=100)
class Manufactor(models.Model):
    name=models.CharField(default='',max_length=100)

class Product(models.Model):
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE,null=True,blank=True)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE,null=True,blank=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True,blank=True)
    manufactor = models.ForeignKey(Manufactor,on_delete=models.CASCADE,null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(default='',max_length=100,null=True,blank=True)
    description = models.TextField(default='',null=True,blank=True)
    active = models.BooleanField(default=False,null=True,blank=True)
    price = models.IntegerField(default=0,null=True,blank=True)
    product_image = models.ImageField(default='',null=True,blank=True)
    date_release = models.CharField(default='',max_length=1000,null=True,blank=True)
    page_number = models.IntegerField(default=0,null=True,blank=True)
    year_release = models.IntegerField(default=0,null=True,blank=True)
    size = models.CharField(default='',max_length=100,null=True,blank=True)
    discriminator = models.CharField(default='',max_length=100,null=True,blank=True)
class Image(models.Model):
    product_image = models.ImageField(default='')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,default='')
class Variation(models.Model):
    title = models.CharField(default='',max_length=1000)
    price = models.IntegerField(default=0)
    sale_price = models.IntegerField(default=0)
    active = models.BooleanField(default=False)
    inventory = models.IntegerField(default=0)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
