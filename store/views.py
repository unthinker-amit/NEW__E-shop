from itertools import product
from django.shortcuts import render
from django.http import HttpResponse
from .models.product_models import Product

# Create your views here.
def index(request):
    products=Product.get_all_product()

    return render(request,'index.html',{'products':products})