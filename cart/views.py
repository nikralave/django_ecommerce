from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from.utils import get_cart_items_and_total

# Create your views here.

def view_cart(request):
    cart=request.session.get('cart', {})
    context = get_cart_items_and_total(cart)
    return render(request, "cart/cart.html", context)
    
    
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
    
    return redirect('get_products')
    
def remove_from_cart(request):
    id = request.POST['product_id']
    product = get_object_or_404(Product, pk=id)
    
    #Get the current Cart
    cart = request.session.get('cart', {})
    
    
    #Update the cart
    if cart[id] <= 1:
         del cart[id]
    else:
        cart[id] =cart.pop(id, 0) - 1
       
    #Save the cart back to the session
    
    
    request.session['cart'] = cart

    return redirect('view_cart')
    