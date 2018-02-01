from django.shortcuts import get_object_or_404
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from orders.models import CustomerOrder

# as laid out in ipn docs we can look for a signal from paypal
# that the order has been paid for, then we can update the order object associated
# with that order number. make sure to use ngrok for local testing
def payment_notification(sender, **kwargs):
	ipn_obj = sender
	if ipn_obj.payment_status == ST_PP_COMPLETED:
		# payment was sucessful
		order = get_object_or_404(CustomerOrder, pk=ipn_obj.invoice)
		order.paid = True
		order.total_cost = order.get_total_cost()
		order.save()

valid_ipn_received.connect(payment_notification)