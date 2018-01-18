from django.shortcuts import render, get_object_or_404
from .models import Product, Photo

def products_view(request, category_pk):
	products = Product.objects.filter(category=category_pk)
	return render(request, 'allproducts.html', {'products': products,})

def product_detail_view(request, product_pk):
	product = get_object_or_404(Product, pk=product_pk)
	return render(request, 'productdetail.html', {'product': product,})