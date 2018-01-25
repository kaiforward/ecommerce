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

	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(self):
		return "Image Slideshow"

class HomeFeature(models.Model):

	product_one = models.ForeignKey(Product, on_delete=models.CASCADE)
	product_two = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_two')
	product_three = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_three')

	def __str__(self):
		return "3 Featured Products"

class HomeCollection(models.Model):

	category_one = models.ForeignKey(Category, on_delete=models.CASCADE)
	category_two = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_two')
	category_three = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_three')
	category_four = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_four')

	def __str__(self):
		return "4 Featured Categories"

class About(models.Model):

	headline =  models.CharField(max_length=50, blank=True, null=True)
	content =  tinymce_models.HTMLField(blank=True, null=True)


