from django.shortcuts import render,HttpResponse
from products.models import Products

# Create your views here.

def signup_view(request):
    return render(request,'dashboard/sign_up.html')

def home_view(request):
    products = list(Products.objects.values())
    
    return render(request,'dashboard/shopping-main-page.html',context={'products':products})