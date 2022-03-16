from django.views import View
from django.shortcuts import redirect
from store.models.product_models import Product
from store.models.order import Order

from store.models.customer import Customer


class Checkout(View):
    def get(self, request):
        customer = request.session.get("customer")
        customer_obj=Customer.objects.get(id=customer)
        phone=customer_obj.phone
        cart = request.session.get("cart")
        products = Product.get_products_by_ids(list(cart.keys()))
        for product in products:
            order = Order(
                customer=customer_obj,
                product=product,
                price=product.price,
                phone=phone,
                quantity=cart.get(str(product.id)),
            )
            order.save()
        request.session["cart"] = {}
        return redirect("cart")
