from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from products.models import Product, ProductAttribute, ProductVariant
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
				 attribute=cd['variant'],
				 update_quantity=cd['update_quantity'],
				 update_variant=cd['update_variant'],
				 )
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
		# try to get product attribute
		attribute = get_object_or_404(ProductAttribute, attribute=item['attribute'])
		# give each item in cart a form to update the quantity or variant of the product
		item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 
			'variant': attribute, 'update_quantity': True, 'update_variant':True, })
		# set the varaint queryset to use the variant associated with product attribute chosen.
		item['update_quantity_form'].fields['variant'].queryset = ProductAttribute.objects.filter(product_variant=attribute.product_variant)
	return render(request, 'cart_detail.html', {'cart': cart})