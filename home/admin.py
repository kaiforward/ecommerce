from django.contrib import admin
from .models import HomeCarousel, HomeFeature, About, NavbarImage

# Register your models here.
admin.site.register(NavbarImage)
admin.site.register(HomeCarousel)
admin.site.register(HomeFeature)
admin.site.register(About)