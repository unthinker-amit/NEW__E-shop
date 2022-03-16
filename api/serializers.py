from rest_framework import serializers
from store.models.product_models import Product


class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price", "category", "description", "image"]
