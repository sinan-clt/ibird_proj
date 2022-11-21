from django.shortcuts import render
from product_app.models import *

# Create your views here.

def listProducts(request):

    products = Product.objects.filter(is_deleted=False).order_by('-created_on')
    all_categories = Category.objects.all()
    categoryID = request.GET.get('category')
    sub_category = request.GET.get('sub_cat')
    if categoryID:
        products = Product.objects.filter(category=categoryID).order_by('-created_on')
    else:
        products = Product.objects.filter(is_deleted=False).order_by('-created_on')
    if sub_category:
        sub_cate = SubCategory.objects.filter(main_category=sub_category)
    else:
        sub_cate = SubCategory.objects.filter(main_category=sub_category)

    return render(request, 'products.html', {'data': products, 'categories':sub_cate,"categories1":all_categories})


def productDetails(request, id):
    
    product = Product.objects.get(id=id)
    return render(request, 'product-detail.html',{'data':product})