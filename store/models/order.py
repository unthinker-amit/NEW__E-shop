from django.db import models
from .product_models import Product
from .customer import Customer
import datetime


class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    date=models.DateField(default=datetime.datetime.today)
    address=models.CharField(max_length=100,default='')
    phone=models.CharField(max_length=12,default='')

