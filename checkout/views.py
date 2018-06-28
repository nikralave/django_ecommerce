from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from products.models import Product
from .forms import OrderForm, MakePaymentForm

# Create your views here.
def checkout(request):
    
    if request.method=="POST":
        order_form = OrderForm(request.POST)
        if form.is_valid():
            order_form.save()
            return HttpResponse("I mad an Order, it's in the DB, go have a look")
    
    else: 
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
            
        order_form = OrderForm()
        payment_form = MakePaymentForm()
    
        return render(request, "checkout/checkout.html", {'cart_items':cart_items, 'total':cart_total, 'order_form':order_form, 'payment_form':payment_form})