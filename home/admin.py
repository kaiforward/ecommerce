from django.contrib import admin
from .models import HomeCarousel, HomeFeature, About, NavbarImage, HomeCollection

# Register your models here.
admin.site.register(NavbarImage)
admin.site.register(HomeCarousel)
admin.site.register(HomeFeature)
admin.site.register(HomeCollection)
admin.site.register(About)