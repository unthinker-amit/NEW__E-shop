from contextlib import redirect_stderr
from itertools import product
from django.shortcuts import render,redirect
from store.models.product_models import Product
from store.models.category import Category
from django.views import View
from django.http import HttpResponse

class Index(View):
    def get(self,request):
        products=Product.get_all_product()
        category=Category.get_all_category()
        category_id=request.GET.get('category')
        if category_id:
            products=Product.get_all_product_by_category_id(category_id)
        return render(request,'index.html',{'products':products,"categories":category})
    def post(self,request):
        product=request.POST.get('product')
        remove=request.POST.get('remove')
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
                if remove:
                    cart[product]=quantity-1
                else:
                    cart[product]=quantity+1
            else:
                cart[product]=1
        else:
            cart={}
            cart[product]=1
        request.session['cart']= cart
        print(request.session['cart'])
        return redirect('homepage')


