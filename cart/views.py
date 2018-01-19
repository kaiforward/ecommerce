from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from products.models import Product
from .cart import Cart
from .forms import CartAddProductForm

# Create your views here.
@require_POST
def cart_add(request, product_pk):
	cart = Cart(request)
	product = get_object_or_404(Product, pk=product_pk)
	form =  CartAddProductForm(request.POST)
	if form.is_valid():
		cd = form.cleaned_data
		cart.add(product=product,
				 quantity=cd['quantity'],
				 update_quantity=cd['update']
				 )
	return redirect('cart_detail')

def cart_remove(request, product_pk):
	cart = Cart(request)
	product = get_object_or_404(Product, pk=product_pk)
	cart.remove(product)
	return redirect('cart_detail')

def cart_detail(request):
	cart = Cart(request)
	for item in cart:
		item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
			'update': True})
	return render(request, 'cart_detail.html', {'cart': cart, 'range': range(20)})