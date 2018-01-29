from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse
from django.conf import settings
from .models import CustomerOrder, CustomerProduct
from products.models import Product
from .forms import OrderForm
from cart.cart import Cart
from decimal import Decimal	
from paypal.standard.forms import PayPalPaymentsForm
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY
import copy


# Create your views here.
def order(request):
	cart = Cart(request)
	# by copying the cart object it is not saved as part of the POST request
	post_cart = copy.deepcopy(cart)
	stripe_key = settings.STRIPE_PUBLIC_KEY
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			order = CustomerOrder.objects.create(
					first_name=cd['first_name'],
					last_name=cd['last_name'],
					email=cd['email'],
					address1=cd['address1'],
					town=cd['town'],
					post_code=cd['postcode'],
					country=cd['country'],
					additional_note=cd['additional_note'],
				)
			order.save()			
			for item in post_cart:
				CustomerProduct.objects.create(customer_order=order,
											   product=item['product'],
											   price=item['price'],
											   attribute=item['attribute'],
											   quantity=item['quantity'],)
			# clear the cart
			cart.clear()
			# launch asynchronous task (email)
			# order_created.delay(order.pk)
			# set the order in the session
			request.session['order_pk'] = order.pk
			#redirect to payment
			return redirect('make_payment')				
	else:
		form = OrderForm()
	return render(request, 'order.html', {'cart': cart, 'form': form, 'stripe_key': stripe_key})
													
def order_created(request, new_order):
	order = new_order
	return render(request, 'order_created.html', {'order': order})

@staff_member_required
def admin_order_detail(request, order_pk):
	order = get_object_or_404(CustomerOrder, pk=order_pk)
	return render(request, 'admin_order_detail.html', {'order': order})