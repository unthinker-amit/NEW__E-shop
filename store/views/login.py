from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from store.models.cart_data import CartDataModel
from store.models.customer import Customer
from django.views import View
from django.contrib.auth.hashers import check_password


class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get("return_url")
        return render(request, "login.html")

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            customer = Customer.objects.get(email=email)
            if customer:
                request.session["customer"] = customer.id
                request.session["name"] = customer.first_name
                request.session["email"] = customer.email
                flag = check_password(password, customer.password)
                if flag:
                    if Login.return_url:
                        return HttpResponseRedirect(Login.return_url)
                    else:
                        Login.return_url = None
                        return redirect("homepage")
        except:
            return render(
                request,
                "login.html",
                {"error": "Email or Password is invalid", "values": {"email": email}},
            )
        return render(
            request,
            "login.html",
            {"error": "Email or Password is invalid", "values": {"email": email}},
        )


def logout(request):
    # cart(request)
    request.session.clear()
    return redirect("login")


def cart(request):
    cart = request.session.get("cart")
    customer = request.session.get("customer")
    customer = Customer.objects.get(id=customer)
    if customer and cart:

        cart_data = CartDataModel(cart_data=cart, customer=customer)
        cart_data.save()
