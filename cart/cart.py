from decimal import Decimal
from django.conf import settings
from products.models import Product

class Cart(object):

	def __init__(self, request):

		"""
		Initialize the cart.
		"""
		self.session = request.session
		cart = self.session.get(settings.CART_SESSION_ID)
		if not cart:
			# Create empty cart if one doesn't exist
			cart = self.session[settings.CART_SESSION_ID] = {}
		self.cart = cart

	def add(self, product, quantity=1, update_quantity=False):
		"""
		Add a product to the cart or update its quantity.
		"""
		product_pk = str(product.pk)
		if product_pk not in self.cart:
			self.cart[product_pk] = {'quantity': 0, 'price': str(product.price)}

		if update_quantity:
			self.cart[product_pk]['quantity'] = quantity
		else:
			self.cart[product_pk]['quantity'] += quantity
		self.save()

	def save(self):

		# update session cart
		self.session[settings.CART_SESSION_ID] = self.cart
		# mark the session as "modified" to make sure it is saved
		self.session.modified = True

	def remove(self, product):
		"""
		Remove a Product from the cart
		"""
		product_pk = str(product.pk)
		if product_pk in self.cart:
			del self.cart[product_pk]
			self.save()

	def __iter__(self):

		"""
		Iterate over items in the cart and get the products from the db
		"""
		product_pks = self.cart.keys()
		# get the product objects and add them to the cart
		products = Product.objects.filter(pk__in=product_pks)
		for product in products:
			self.cart[str(product.pk)]['product'] = product

		for item in self.cart.values():
			item['price'] = Decimal(item['price'])
			item['total_price'] = item['price'] * item['quantity']
			yield item

	def __len__(self):
		"""
		Countall items in the cart
		"""
		return sum(item['quantity'] for item in self.cart.values())

	def get_total_price(self):
		return sum(Decimal(item['price']) * item['qauntity'] for item in self.cart.values())