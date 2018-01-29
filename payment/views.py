from decimal import Decimal
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from orders.models import CustomerOrder, CustomerProduct
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY
import logging

@csrf_exempt
def paypal_done(request):
	return render(request, "paypal_done.html")

@csrf_exempt
def paypal_cancelled(request):
	return render(request, "paypal_cancelled.html")

def make_payment(request):

	order_pk = request.session.get('order_pk')
	order = get_object_or_404(CustomerOrder, pk=order_pk)
	products = CustomerProduct.objects.filter(customer_order=order)
	host = request.get_host()
	
	stripe_dict = {
	'stripe_key': settings.STRIPE_PUBLIC_KEY,
	'data_name': 'Eva Brudenell',
	# stripe requires amount in pence as int
	'amount': '{}'.format(int(order.get_total_cost()*100)),
	'item_name': 'Order {}'.format(order_pk),
	}
	
	paypal_dict = {
	'business': settings.PAYPAL_RECEIVER_EMAIL,
	# get decimal amount for paypal
	'amount': '%.2f' % order.get_total_cost(),
	'item_name': 'Order {}'.format(order_pk),
	'invoice': str(order.pk),
	'currency_code': 'GBP',
	'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
	'return_url': 'http://{}{}'.format(host, reverse('paypal_done')),
	'cancel_return': 'http://{}{}'.format(host, reverse('paypal_cancelled'))
	}	
	form = PayPalPaymentsForm(initial=paypal_dict)

	return render(request, 'make_payment.html', {'order': order, 'form': form, 'stripe_dict': stripe_dict, 'paypal_dict': paypal_dict})

@csrf_exempt
def stripe_payment(request):

	order_pk = request.session.get('order_pk')
	order = get_object_or_404(CustomerOrder, pk=order_pk)
	products = CustomerProduct.objects.filter(customer_order=order)
	order_meta = {'name': order.first_name + ' ' + order.last_name,
				  'email': order.email,
				  'address': order.address1+', '+order.town+', '+order.country,
				  'postcode': order.post_code,
				  'order number': order.pk,
				  'note': order.additional_note,}
	if len(products) < 15:	
		for product in products:
			order_meta[product.product.name] = 'quantity={}, attribute={}'.format(product.quantity, product.attribute) 
	else:
		order_meta['products'] = 'Quantity of order too large in include in stripe metadata.'

	if request.method == "POST":
	    token = request.POST.get("stripeToken")

	try:
	    charge = stripe.Charge.create(
	        amount=int(order.get_total_cost()*100),
	        currency="gbp",
	        source= token,
	        description= 'Order {}'.format(order_pk),
			metadata= order_meta,
	    )

	except stripe.error.CardError as e:
		# Since it's a decline, stripe.error.CardError will be caught
		body = e.json_body
		err  = body.get('error', {})

		print ("Status is: %s" % e.http_status)
		print ("Type is: %s" % err.get('type'))
		print ("Code is: %s" % err.get('code'))
		# param is '' in this case
		print ("Param is: %s" % err.get('param'))
		print ("Message is: %s" % err.get('message'))
	except stripe.error.RateLimitError as e:
		# Too many requests made to the API too quickly
		pass
	except stripe.error.InvalidRequestError as e:
		# Invalid parameters were supplied to Stripe's API
		pass
	except stripe.error.AuthenticationError as e:
		# Authentication with Stripe's API failed
		# (maybe you changed API keys recently)
		pass
	except stripe.error.APIConnectionError as e:
		# Network communication with Stripe failed
		pass
	except stripe.error.StripeError as e:
		# Display a very generic error to the user, and maybe send
		# yourself an email
		pass
	except Exception as e:
		# Something else happened, completely unrelated to Stripe
		pass
	else:
		if charge:
			order.paid = True
			order.stripe_id = charge.id
			order.save()
		return redirect("stripe_done")
	    # The payment was successfully processed, the user's card was charged.
	    # as well as updated the paid boolean, we add the stripe_id to the charge for reference.

@csrf_exempt
def stripe_done(request):
	order_pk = request.session.get('order_pk')
	order = get_object_or_404(CustomerOrder, pk=order_pk)

	return render(request, "stripe_done.html", {'order': order})

def checkout(request):

    new_car = Car(
        model = "Honda Civic",
        year  = 2017
    )

    if request.method == "POST":
        token    = request.POST.get("stripeToken")

    try:
        charge  = stripe.Charge.create(
            amount      = 2000,
            currency    = "usd",
            source      = token,
            description = "The product charged to the user"
        )

        new_car.charge_id   = charge.id

    except stripe.error.CardError as ce:
        return False, ce

    else:
        new_car.save()
        return redirect("thank_you_page")
        # The payment was successfully processed, the user's card was charged.
        # You can now redirect the user to another page or whatever you want







	

