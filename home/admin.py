from django.contrib import admin
from .models import HomeCarousel, HomeFeatured, About

# Register your models here.
admin.site.register(HomeCarousel)
admin.site.register(HomeFeatured)
admin.site.register(About)