from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [

	path('view/', views.cart_detail, name='cart_detail'),
	path('add/<product_pk>/', views.cart_add, name='cart_add'),
	path('remove/<product_pk>/', views.cart_remove, name='cart_remove'),
]