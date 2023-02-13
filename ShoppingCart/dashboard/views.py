from django.shortcuts import render,HttpResponse,redirect
from products.models import *
import json
from django.core import serializers
from django.forms.models import model_to_dict
from .forms import ShippingDetailsForm
from datetime import date
# Create your views here.



def signup_view(request):
    return render(request,'dashboard/sign_up.html')

def home_view(request):
    request.session['Cart'] = None
    products = list(Product.objects.values())
    
    return render(request,'dashboard/shopping-main-page.html',context={'products':products})

def store_cart_data_view(request):
    cart_items = request.GET.get('cartItems',None)
    request.session['Cart'] = cart_items
    
    return HttpResponse("Stored data successfully")
    

def cart_view(request):
   
    cart_items = request.session.get('Cart',None)
    
    cart_items = json.loads(cart_items)
    
    cart_list = []
    total_purchase_amount = 0
    
    for item in cart_items:
        product = Product.objects.get(id=item['id'])
       
        product_dict = model_to_dict(product,fields=['name','image','price','description'])
        product_dict['quantity'] = item['quantity']
        total_purchase_amount += item['quantity'] * product_dict['price']
        cart_list.append(product_dict)
    
    if cart_items:
        context = {
            "cart_items":cart_list,
            "total":total_purchase_amount,
        }
        request.session['cart-details'] = cart_list
        
        request.session['total'] = total_purchase_amount
    else:
        context = {"cart_items":[]}

    return render(request,'dashboard/cart.html',context=context)

def checkout_view(request):
    cart_details = request.session.get('cart-details',None)
    total = request.session.get('total',None)
    
    form = ShippingDetailsForm()
    
    if request.method == "GET":
        context = {
                "cart_items":cart_details,
                "total":total,
                "form":form
            }
        return render(request,'dashboard/checkout.html',context=context)
    else :
        form  = ShippingDetailsForm(request.POST)
       
        if form.is_valid():
            address = form.cleaned_data.get('address')
            state = form.cleaned_data['state']
            city = form.cleaned_data['city']
            zipcode = form.cleaned_data['zipcode']
            curr_user = User.objects.get(username=request.user)
            order_id = uuid.uuid4()
            order = Order(order_id=order_id,user_id=curr_user,order_date=date.today(),total_purchase_amount=total,address=address,state=state,city=city,zipcode=zipcode)
            order.save()
            order.refresh_from_db()
           
            for item in cart_details:
                total_price = item['quantity'] * item['price']
                product = Product.objects.get(name=item['name'])
                
                order_details = OrderDetail(order_id=order,product_id=product,quantity=item['quantity'],unit_price=item['price'],total_price=total_price)
                order_details.save()
            
            print("Sucessfully saved all the data")
            return redirect('home')
            
def order_history_view(request):
    user = User.objects.get(username=request.user)
    
    orders = Order.objects.filter(user_id=user.id)
    if orders:
        orders_list = []
        for order in orders:
            orderDetails = OrderDetail.objects.filter(order_id=order)
            orderDetails_copy = model_to_dict(orderDetails)
            product = Product.objects.get(id=orderDetails_copy['product_id'])
            product_dict = product.__dict__
            product_name = product_dict['name']
            orderDetails_copy['name'] = product_name
            orders_list.append(orderDetails_copy)
            
       
        
        context = {
            "orders_list":orders_list
        }
    else:
        context = {
            "orders_list":[]
        }

    return render(request,'dashboard/order_history.html',context=context)