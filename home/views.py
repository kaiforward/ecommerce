from django.shortcuts import render, get_object_or_404

from products.models import Product, Category
from .models import HomeCarousel, HomeFeature, About, HomeCollection
from blog .models import Blog

# Create your views here.
def home_view(request):
	blogs = Blog.objects.order_by('-date')
	home_carousel = get_object_or_404(HomeCarousel)
	featured_products = get_object_or_404(HomeFeature)
	featured_categories = get_object_or_404(HomeCollection)
	return render(request, 'index.html', {'home_carousel': home_carousel, 'featured_products': featured_products, 'blogs': blogs, 'featured_categories': featured_categories,})

def about_view(request):
	about_info = get_object_or_404(About)
	return render(request, 'about.html', {'about_info': about_info})