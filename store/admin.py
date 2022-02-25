import imp
from unicodedata import category
from django.contrib import admin
from .models.product_models import Product
from .models.category import Category

# Register your models here.
@admin.register(Product)
class admin_dis(admin.ModelAdmin):
    list_display=['name','category','price']


@admin.register(Category)
class admin_cat(admin.ModelAdmin):
    list_display=['name']
