from django.db import models
from products.models import Product
from decimal import Decimal

class CustomerOrder(models.Model):

	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	# shipping details
	address1 = models.CharField(max_length=100)
	town = models.CharField(max_length=100)
	country = models.CharField(max_length=200)
	post_code = models.CharField(max_length=8)
	paid = models.BooleanField(default=False)
	additional_note = models.CharField(max_length=200, blank=True, null=True)
	shipping_type = models.CharField(max_length=100, default='')
	stripe_id = models.CharField(max_length=100, default = '')
	total_cost = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('-date_created',)

	def __str__(self):
		return 'Order {}'.format(self.pk)

	def get_total_cost(self):
		return sum(item.get_cost() for item in self.items.all())

class CustomerProduct(models.Model):
	# objects given related names they can be iterated by by get total_cost method
	customer_order = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE, related_name='items')
	price = models.DecimalField(max_digits=10, decimal_places=2)
	product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE, related_name='order_items')
	attribute = models.CharField(max_length=50)
	quantity = models.CharField(max_length=50)

	def __str__(self):
		return str(self.pk)

	def get_cost(self):
		return Decimal(self.price) * Decimal(self.quantity)

class Shipping(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class ShippingChoice(models.Model):
	shipping = models.ForeignKey(Shipping, on_delete=models.CASCADE, related_name='shipping_items')
	description = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=5, decimal_places=2, default=0)