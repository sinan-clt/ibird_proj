from django.urls import path
from . import views

urlpatterns = [
    path('', views.listProducts, name='listProducts'),
    path('product_detail/<int:id>', views.productDetails, name='productDetails'),
]