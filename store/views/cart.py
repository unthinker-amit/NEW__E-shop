from django.views import View
from django.shortcuts import render
from store.models.product_models import Product

class Cart(View):
    def get(self,request):
        ids=list(request.session.get('cart').keys())
        products=Product.get_products_by_ids(ids)
        print(products)
        return render(request,'cart.html',{'products':products})