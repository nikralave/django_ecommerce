from django.urls import path
from .views import get_cart, add_to_cart

urlpatterns = [
    path('cart/view', get_cart, name= 'get_cart'),
     path('cart/add', add_to_cart, name='add_to_cart'),
    ]