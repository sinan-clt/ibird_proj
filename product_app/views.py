from django.shortcuts import render
from product_app.models import *


# Create your views here.

def listProducts(request):
    if request.method == 'GET':
        products = Product.objects.filter(is_deleted=False).order_by('-created_on')
    return render(request, 'products.html', {'data': products})