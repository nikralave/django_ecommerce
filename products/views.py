from django.shortcuts import render, get_object_or_404, redirect
from .models import Product


# Create your views here.

def get_products(request):
    products = Product.objects.all()
    return render(request, "products/products.html", {'products': products})
    
