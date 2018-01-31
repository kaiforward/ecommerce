from django.db import models
from tinymce import models as tinymce_models

# Create your models here.
class Blog(models.Model):

	headline = models.CharField(max_length=50)
	image = models.ImageField(upload_to='blog', blank=True, null=True)
	description = tinymce_models.HTMLField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.headline