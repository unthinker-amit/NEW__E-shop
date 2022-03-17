from django.shortcuts import render
from django.http import HttpResponse
from store.models.product_models import Product
from .serializers import productSerializer
from rest_framework import viewsets
from api import serializers

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class ListView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = productSerializer


class RUDView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = productSerializer


def home(request):
    return HttpResponse("hello")
