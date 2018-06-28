from django.shortcuts import get_object_or_404
from products.models import Product
from decimal import Decimal

def get_cart_items_and_total(cart):
    cart_total = 0
    # cart_items is passing the list of products to the html if we use cart_items in html to do it 
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
    

    return { 'cart_items': cart_items, 'total': cart_total }
    