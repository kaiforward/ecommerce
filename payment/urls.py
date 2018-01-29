from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
	path('choose/', views.make_payment, name='make_payment'),
	path('done/', views.paypal_done, name='paypal_done'),
	path('cancelled/', views.paypal_cancelled, name='paypal_cancelled'),
	path('stripe_payment/', views.stripe_payment, name='stripe_payment'),
	path('complete/', views.stripe_done, name='stripe_done'),	
]