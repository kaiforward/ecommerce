from django.db import models
from tinymce import models as tinymce_models


class Category(models.Model):

	name = models.CharField(max_length=50, blank=True, null=True)
	image = models.ImageField(upload_to='productimages', blank=True, null=True)
	description = tinymce_models.HTMLField()

	def __str__(self):
		return self.name

class ProductVariant(models.Model):
	# product to assign new choosable attributes to.
	variant_name = models.CharField(max_length=50)

	def __str__(self):
		return self.variant_name

class Product(models.Model):

	name = models.CharField(max_length=50)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	description = tinymce_models.HTMLField()
	price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	stock = models.IntegerField(default=0)
	quantity = models.IntegerField(default=0)
	variant = models.ForeignKey(ProductVariant, blank=True, null=True, on_delete=models.PROTECT)
	variant_two = models.ForeignKey(ProductVariant, blank=True, null=True, on_delete=models.PROTECT, related_name='variant_two')
	variant_three = models.ForeignKey(ProductVariant, blank=True, null=True, on_delete=models.PROTECT, related_name='variant_three')

	def __str__(self):
		return self.name + ' - ' + self.category.name

class ProductAttribute(models.Model):
	# create a specific attribute to assign to product variant. E.g Large for shirts.
	product_variant = models.ForeignKey(ProductVariant, blank=True, null=True, on_delete=models.CASCADE)
	attribute = models.CharField(max_length=50)

	def __str__(self):
		return self.attribute

class Photo(models.Model):

	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='productimages', blank=True, null=True)

	def __str__(self):
		return self.product.name