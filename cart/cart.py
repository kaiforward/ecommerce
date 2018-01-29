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

	def add(self, product, attribute, quantity=1, update_quantity=False, update_variant=False):
		"""
		Add a product to the cart or update its quantity.
		"""

		# set product attributes
		if attribute == None:
			attribute = 'none'
		else:
			attribute = attribute.attribute

		product_pk = str(product.pk)
		if product_pk not in self.cart:
			self.cart[product_pk] = {'quantity': 0, 'price': str(product.price)}

		if update_quantity:
			self.cart[product_pk]['quantity'] = quantity			
		else:
			self.cart[product_pk]['quantity'] += quantity

		if update_variant:
				self.cart[product_pk]['attribute'] = attribute
		else:
				self.cart[product_pk]['attribute'] = attribute
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
			item['price'] = (Decimal(item['price']))
			item['total_price'] = item['price'] * item['quantity']
			yield item
			self.session.modified = False

	def __len__(self):
		"""
		Countall items in the cart
		"""
		return sum(item['quantity'] for item in self.cart.values())

	def get_total_price(self):
		return (sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values()))

	def clear(self):
		#empty cart
		self.session[settings.CART_SESSION_ID] = {}
		self.session.modified = True

class Shipping(object):

	def __init__(self, request):

		"""
		Initialize the cart.
		"""
		self.session = request.session
		shipping = self.session.get(settings.SHIPPING_SESSION_ID)
		if not shipping:
			# Create empty shipping info if one doesn't exist
			shipping = self.session[settings.SHIPPING_SESSION_ID] = {}
		self.shipping = shipping

	def add_shipping_details(self, 
							first_name, 
							last_name,
							email, 
							address1, 
							town, 
							postcode, 
							country, 
							additional_note,):
		"""
		Add Cart Shipping details.
		"""
		self.shipping['shipping'] = {
			'first_name': str(first_name),
			'last_name': str(last_name),
			'email': str(email),
			'address1': str(address1),
			'town': str(town),
			'postcode': str(postcode),
			'country': str(country),
			'additional_note': str(additional_note),
		}

		self.save()

	def save(self):

		# update session shipping details.
		self.session[settings.SHIPPING_SESSION_ID] = self.shipping
		# mark the session as "modified" to make sure it is saved.
		self.session.modified = True

	def __iter__(self):

		"""
		Iterate over items in the cart and get the products from the db
		"""
		for item in self.shipping.values():
			yield item