from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.views import View
from django.contrib.auth.hashers import make_password

# Create your views here.
class Sign_up(View):
    def get(self, request):
        return render(request, "sign_up.html")

    def post(self, request):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        password = request.POST.get("password")
        customer = Customer(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            password=password,
        )

        # validation
        value = {
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "email": email,
        }
        error_message = None

        customer = Customer(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
            password=password,
        )
        error_message = self.validateCustomer(customer)

        if not error_message:
            # print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            # customer.register()
            customer.save()
            return redirect("homepage")
        else:
            data = {"error": error_message, "values": value}
            return render(request, "sign_up.html", data)

    def validateCustomer(self, customer):
        error_message = None
        if not customer.first_name:
            error_message = "First Name Required !!"
        elif len(customer.first_name) < 4:
            error_message = "First Name must be 4 char long or more"
        elif not customer.last_name:
            error_message = "Last Name Required"
        elif len(customer.last_name) < 4:
            error_message = "Last Name must be 4 char long or more"
        elif not customer.phone:
            error_message = "Phone Number required"
        elif len(customer.phone) < 10:
            error_message = "Phone Number must be 10 char Long"
        elif len(customer.password) < 6:
            error_message = "Password must be 6 char long"
        elif len(customer.email) < 5:
            error_message = "Email must be 5 char long"
        elif customer.isExists():
            error_message = "Email Address Already Registered.."
        # saving
        return error_message
