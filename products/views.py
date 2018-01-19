from django.shortcuts import render, get_object_or_404
from .models import Product, Photo
from cart.forms import CartAddProductForm

def products_view(request, category_pk):
	products = Product.objects.filter(category=category_pk)
	return render(request, 'allproducts.html', {'products': products,})

def product_detail_view(request, product_pk):
	product = Product.objects.filter(pk=product_pk)[0]
	cart_product_form = CartAddProductForm()
	return render(request, 'productdetail.html', {'product': product, 
													'cart_product_form': cart_product_form,})