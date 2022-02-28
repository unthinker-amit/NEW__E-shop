from django.views import View
from django.shortcuts import redirect
from store.models.product_models import Product
from store.models.order import Order

from store.models.customer import Customer





class Checkout(View):
    def post(self,request):
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        customer=request.session.get('customer')
        cart=request.session.get('cart')
        products=Product.get_products_by_ids(list(cart.keys()))
        print(address, phone, customer, cart, products)
        for product in products:
            order=Order(customer=Customer(id=customer),
            product=product,
            price=product.price,
            phone=phone,
            address=address,
            quantity=cart.get(str(product.id))
            )
            order.save()
        request.session['cart']={}
        return redirect('cart')