from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Product , cake_list
from .cart import Cart
from .forms import CartAddProductForm
from django.contrib.auth.decorators import login_required


from products.forms import make_order_form
# Create your views here.

@login_required(login_url="/login/")
@require_POST
def cart_add(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(cake_list,id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add( product=product,quantity=cd['quantity'],override_quantity=cd['override'])
    return redirect('cart:cart_detail')

def cart_remove(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(cake_list,id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)

    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity':item['quantity'],'override':True})
    return render(request,'cart/detail.html',{'cart':cart,'make_order_form':make_order_form})
    