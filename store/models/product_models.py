from email.policy import default
from django.db import models
from .category import Category

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default="", null=True, blank=True)
    image = models.ImageField(upload_to="uploads/product/", default=None)

    @staticmethod
    def get_all_product():
        return Product.objects.all()

    @staticmethod
    def get_all_product_by_category_id(category_id):
        return Product.objects.filter(category_id=category_id)

    @staticmethod
    def get_products_by_ids(ids):
        return Product.objects.filter(id__in=ids)
