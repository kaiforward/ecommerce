import itertools

from django.shortcuts import get_object_or_404
from django.conf import settings
from .models import NavbarImage

def nav_homepage(request):
	"""
    Return Categories for use by Navbar
    """
	return {'navbar_content': NavbarImage.objects.all()}