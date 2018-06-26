from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from django.http import HttpResponse

# Create your views here.

def get_cart(request):
    return render(request, "cart/cart.html")
    
def add_to_cart(request):
    
    #Get the product we're adding
    id = request.POST['product_id']
    product = get_object_or_404(Product, pk=id)
    
    #Get the current Cart
    cart = request.session.get('cart', {})
    
    #Update the cart
    cart[id] =cart.get(id, 0) + 1
    
    #Save the cart back to the session
    request.session['cart'] = cart
    
    return HttpResponse(cart[id])