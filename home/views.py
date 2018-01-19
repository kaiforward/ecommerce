from django.shortcuts import render, get_object_or_404

from products.models import Product, Category
from .models import HomeCarousel, HomeFeature, About
from blog .models import Blog

# Create your views here.
def home_view(request):
	blogs = Blog.objects.order_by('-date')
	home_carousel = HomeCarousel.objects.all()[0]
	featured_products = HomeFeature.objects.all()[0]
	featured_categories = Category.objects.all()[0:4]
	return render(request, 'index.html', {'home_carousel': home_carousel, 'featured_products': featured_products, 'blogs': blogs, 'featured_categories': featured_categories,})

def about_view(request):
	about_info = HomeFeature.objects.all()[0]
	return render(request, 'about.html', {'about_info': about_info})