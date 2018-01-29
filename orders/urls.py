from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
	path('order/', views.order, name='order'),
	path('admin/order/<order_pk>/', views.admin_order_detail, name='admin_order_detail')
]