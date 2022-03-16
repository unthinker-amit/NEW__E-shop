from contextlib import redirect_stderr
from importlib.metadata import requires
from itertools import product
from django.shortcuts import render, redirect
from pkg_resources import Requirement
from store.models.product_models import Product
from store.models.category import Category
from django.views import View
from django.http import HttpResponse


class Index(View):
    def get(self, request):
        orderBy='date'
        cart = request.session.get("cart")
        if not cart:
            request.session["cart"] = {}
        products = Product.get_all_product().order_by(orderBy)
        category = Category.get_all_category()
        category_id = request.GET.get("category")
        order = request.GET.get("orderBy")
        if not order:
            order='date'
        if category_id:
            products = Product.get_all_product_by_category_id(category_id).order_by(order)
        return render(
            request, "index.html", {"products": products, "categories": category}
        )

    def post(self, request):
        product = request.POST.get("product")
        remove = request.POST.get("remove")
        cart = request.session.get("cart")
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity == 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session["cart"] = cart
        print(request.session["cart"])
        return redirect("homepage")
