from django.db import models
from store.models import Product
from store.models import Customer


class CartDataModel(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cart_data = models.JSONField()

    @staticmethod
    def get_cart_by_customer(customer_id):
        return CartDataModel.objects.filter(customer=customer_id).order_by("-date")
