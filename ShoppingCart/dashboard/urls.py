from django.urls import path 
from .views import *

urlpatterns = [
    path('signup',signup_view,name="signup"),
    path('home',home_view,name="home"),
]