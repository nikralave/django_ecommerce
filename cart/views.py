from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from django.http import HttpResponse

# Create your views here.

def view_cart(request):
    cart=request.session.get('cart', {})
    
    cart_total = 0
    cart_items = []
    for key in cart:
        trainer = get_object_or_404(Product, pk=key)
        
        cart_item = {
            'product':trainer,
            'quantity':cart[key],
            'total': (trainer.price * cart[key])
        }
        cart_items.append(cart_item)
        
        cart_total += cart_item['total']
       
    # cart_items is passing the list of products to the html if we use cart_items in html to do it        
    return render(request, "cart/cart.html", {'cart_items':cart_items, 'total':cart_total})
    
    
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
    
    return redirect('view_cart')
    
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
    