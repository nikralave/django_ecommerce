from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from products.models import Product
from .forms import OrderForm, MakePaymentForm
from .models import OrderLineItem
from cart.utils import get_cart_items_and_total
from django.conf import settings

# Create your views here.
def checkout(request):
    
    if request.method=="POST":
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save()
            
            cart = request.session.get('cart', {})
            for product_id, quantity in cart.items():
                line_item = OrderLineItem()
                line_item.order = order
                product = get_object_or_404(Product, pk=product_id)
                line_item.product = product 
                line_item.quantity = quantity
                line_item.save()
                
            #clear the cart
            del request.session['cart']
        
        return HttpResponse("I mad an Order, it's in the DB, go have a look")
    
    else: 
        cart=request.session.get('cart', {})
        context = get_cart_items_and_total(cart)
            
        order_form = OrderForm()
        payment_form = MakePaymentForm()
        forms = {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE}
        
        context.update(forms)
        return render(request, "checkout/checkout.html", context)