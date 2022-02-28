from django.shortcuts import render
from store.models.product_models import Product
from store.models.category import Category

# Create your views here.
def index(request):
    products=Product.get_all_product()
    category=Category.get_all_category()
    category_id=request.GET.get('category')
    if category_id:
        products=Product.get_all_product_by_category_id(category_id)
    return render(request,'index.html',{'products':products,"categories":category})

