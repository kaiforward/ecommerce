import itertools

from django.conf import settings
from .models import Category

#  custom context processors let me choose variables that can acessed site wide.
# for example this is a good way to give base.html access to certain info on every page

def nav_categories(request):
	"""
    Return Categories for use by Navbar
    """
	return {'categories': Category.objects.all()}