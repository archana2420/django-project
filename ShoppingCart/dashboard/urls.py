from django.urls import path 
from .views import *

urlpatterns = [
    path('signup',signup_view,name="signup"),
    path('home',home_view,name="home"),
    path('store-cart-data',store_cart_data_view,name="store_cart_data"),
    path('cart',cart_view,name="cart"),
    path('checkout',checkout_view,name='checkout'),
    path('order-history',order_history_view,name='order_history')
]