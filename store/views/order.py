from django.views import View
from django.shortcuts import redirect,render
from store.models.product_models import Product
from store.models.order import Order

from store.models.customer import Customer





class Orders(View):
    def get(self,request):
        customer= request.session.get('customer')
        orders=Order.get_order_by_customer(customer)
        return render(request,'order.html',{'orders':orders})