from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
	path('order/', views.order, name='order'),
	path('order/created/<new_order>/', views.order_created, name='order_created'),
]