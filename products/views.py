from django.shortcuts import render, get_object_or_404
from .models import Product, Photo, ProductAttribute
from cart.forms import CartAddProductForm
import random

def products_view(request, category_pk):
	products = Product.objects.filter(category=category_pk)
	return render(request, 'allproducts.html', {'products': products,})

def product_detail_view(request, product_pk):
	product = Product.objects.filter(pk=product_pk)[0]
	cart_product_form = CartAddProductForm()
	products = Product.objects.filter(category=product.category)
	random_products = random.sample(list(products), 4)
	# set variant query set according to the product - this took ages to find out!!!
	cart_product_form.fields['variant'].queryset = ProductAttribute.objects.filter(product_variant=product.variant)

	return render(request, 'productdetail.html', {'product': product, 
												  'cart_product_form': cart_product_form,
												  'random_products': random_products,})