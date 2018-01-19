import itertools

from django.shortcuts import get_object_or_404
from django.conf import settings
from .models import NavbarImage

def nav_homepage(request):
	"""
    Return Categories for use by Navbar
    """
	navbar_content = NavbarImage.objects.all()[0]
	return {'navbar_content': navbar_content}