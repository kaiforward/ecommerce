from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from products.models import Product, ProductAttribute, ProductVariant
from .cart import Cart, Shipping
from .forms import CartAddProductForm
from django.conf import settings
from django.contrib import messages
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY
import logging


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
				 attribute=cd['variant'],
				 update_quantity=cd['update_quantity'],
				 update_variant=cd['update_variant'],
				 )	
	else: 
		logging.error('form not valid')
	return redirect('cart_detail')

def cart_remove(request, product_pk):
	cart = Cart(request)
	product = get_object_or_404(Product, pk=product_pk)
	cart.remove(product)
	return redirect('cart_detail')

def cart_detail(request):

	cart = Cart(request)
	# get session cart
	for item in cart:
		# Okay seems hacky.

		# if product has an attribute
		if item['attribute'] != 'none':
			# find attribute
			attribute = get_object_or_404(ProductAttribute, attribute=item['attribute'])
			# give each item in cart a form to update the quantity or variant of the product
			item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 
				'variant': attribute, 'update_quantity': True, 'update_variant':True, })
			# set the varaint queryset to use the variant associated with product attribute chosen.
			item['update_quantity_form'].fields['variant'].queryset = ProductAttribute.objects.filter(product_variant=attribute.product_variant)
		else:
			# use items without looking up attributes
			item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 
				'variant': item['attribute'], 'update_quantity': True, 'update_variant':True, }) 

	return render(request, 'cart_detail.html', {'cart': cart})

def test_order(request):

	cart = Cart(request)
	shipping = Shipping(request)

	return render(request, 'test_order.html', {'cart': cart, 'shipping': shipping})