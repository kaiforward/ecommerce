from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

	path('all_posts', views.posts_all_view, name='posts_all_view'),

]