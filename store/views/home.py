from django.shortcuts import render, redirect
from store.models.product_models import Product
from store.models.category import Category
from django.views import View


class Index(View):
    def get(self, request):
        order = request.GET.get("orderBy")
        if not order:
            order = "date"
        cart = request.session.get("cart")
        if not cart:
            request.session["cart"] = {}
        products = Product.get_all_product().order_by(order)
        category = Category.get_all_category()
        category_id = request.GET.get("category")
        all = request.GET.get("all")
        if all == "all":
            request.session["cat_id"] = None
        if category_id:
            request.session["cat_id"] = category_id

        cat_id = request.session.get("cat_id")
        if cat_id:
            products = Product.get_all_product_by_category_id(cat_id).order_by(order)
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
