from django.db import models

from products.models import Product, Category
from tinymce import models as tinymce_models

# Create your models here.

class HomeCarousel(models.Model):

	category = models.OneToOneField(Category, on_delete=models.CASCADE, primary_key=True)

	def __str__(self):
		return self.category.name

class HomeFeatured(models.Model):

	product_one = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
	product_two = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True, related_name='product_two')
	product_three = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True, related_name='product_three')

	def __str__(self):
		return "Featured"

class About(models.Model):

	headline =  models.CharField(max_length=50, blank=True, null=True)
	content =  tinymce_models.HTMLField(blank=True, null=True)
