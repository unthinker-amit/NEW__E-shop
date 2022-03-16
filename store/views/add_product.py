from django.views import View
from django.shortcuts import render, redirect
from store.models.product_models import Product
from store.models.category import Category
from django.core.files.storage import FileSystemStorage
from store.form import AddProduct

class app_product(View):
    def get(self, request):
        form=AddProduct()
        return render(request,"add_product.html",{"form":form})
        # categories = Category.objects.all()
        # return render(request, "add_product.html", {"categories": categories})

    def post(self, request):
        form=AddProduct(request.POST)
        if form.is_valid():
                name = request.POST.get("name")
                price = request.POST.get("price")
                category = request.POST.get("category")
                description = request.POST.get("description")
                image = request.FILES.get("image")
                product = Product(
                    name=name,
                    price=price,
                    category=Category.objects.get(id=category),
                    description=description,
                    image=image,
                )
                product.save()

                return redirect("homepage")
        else:
            return render(request,"add_product.html",{"form":form})
