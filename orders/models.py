from django.db import models
from products.models import Product

class CustomerOrder(models.Model):

	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	# shipping details
	address1 = models.CharField(max_length=100)
	town = models.CharField(max_length=100)
	country = models.CharField(max_length=100)
	post_code = models.CharField(max_length=8)
	paid = models.BooleanField(default=False)
	additional_note = models.CharField(max_length=200, blank=True, null=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('-date_created',)

	def __str__(self):
		return self.first_name + ' ' + self.last_name

	def get_total_cost(self):
		return sum(item.get_cost() for item in self.items.all())

class CustomerProduct(models.Model):
	customer_order = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE)
	attribute = models.CharField(max_length=50)
	quantity = models.CharField(max_length=50)