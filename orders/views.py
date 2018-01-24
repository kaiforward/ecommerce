from django.shortcuts import render, redirect
from .models import CustomerOrder, CustomerProduct
from .forms import OrderForm
from cart.cart import Cart

# Create your views here.
def order(request):
	cart = Cart(request)
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
			for item in cart:
				CustomerProduct.objects.create(customer_order=order,
											   product=item['product'],
											   price=item['price'],
											   attribute=item['attribute'],
											   quantity=item['quantity'],)

			# clear the cart
			cart.clear()
			# launch asynchronous task
			# order_created.delay(order.pk)
			return redirect('order_created', order.pk)
				
	else:
		form = OrderForm()
	return render(request, 'order.html', {'cart': cart, 'form': form})
													
def order_created(request, new_order):
	order = new_order
	return render(request, 'order_created.html', {'order': order,})