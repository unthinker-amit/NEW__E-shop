from django.shortcuts import render,redirect
from store.models.customer import Customer
from django.views import View
from django.contrib.auth.hashers import check_password


class Login(View):
    def get(self,request):
        return render(request,'login.html')
    
    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            customer = Customer.objects.get(email=email)
            if customer:
                request.session['customer']= customer.id
                request.session['name']= customer.first_name
                request.session['email']=customer.email
                flag=check_password(password,customer.password)
                if flag:
                    return redirect("homepage")
        except:
            return render(request,'login.html',{'error':'Email or Password is invalid','values':{'email':email}})
        return render(request,'login.html',{'error':'Email or Password is invalid','values':{'email':email}})


def logout(request):
    request.session.clear()
    return redirect('login')