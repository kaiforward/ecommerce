from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [

	path('all/(<category_pk>)/', views.products_view, name='productsall'),
	# confused slightly using new 2.0 pathing, i think this is correct.
	path('detail/(<product_pk>)/', views.product_detail_view, name='productdetail'),

]