from django.views import View
from django.shortcuts import redirect, render
from store.models.product_models import Product
from store.models.order import Order


class Orders(View):
    def get(self, request):
        customer = request.session.get("customer")
        order_id = request.GET.get("order_id")
        if order_id:
            Order.objects.get(id=order_id).delete()
            return redirect("orders")
        orders = Order.get_order_by_customer(customer)
        return render(request, "order.html", {"orders": orders})

        