from django.shortcuts import redirect
from store.models.order import Order
from django.views import View


class Delete_order(View):
    def delete(self, request):
        order_id = request.GET.get("order_id")
        if order_id:
            Order.objects.get(id=order_id).delete()
            return redirect("orders")
