from django.db import models

from products.models import Product, Category
from tinymce import models as tinymce_models

# Create your models here.

class NavbarImage(models.Model):

	headline = models.CharField(max_length=50, blank=True, null=True)
	image = models.ImageField(upload_to='navigation', blank=True, null=True)

	def __str__(self):
		return "Header Title and Image"	

class HomeCarousel(models.Model):

	category = models.OneToOneField(Category, on_delete=models.CASCADE, primary_key=True)

	def __str__(self):
		return "Image Slideshow"

class HomeFeature(models.Model):

	product_one = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
	product_two = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True, related_name='product_two')
	product_three = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True, related_name='product_three')

	def __str__(self):
		return "3 Featured Products"

class About(models.Model):

	headline =  models.CharField(max_length=50, blank=True, null=True)
	content =  tinymce_models.HTMLField(blank=True, null=True)


