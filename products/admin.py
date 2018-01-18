# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Category, Product, Photo, ProductVariant, ProductAttribute

# set photo class as "inline" meaning photo's cant be edited on product admin page.
class PhotoInline(admin.StackedInline):
    model = Photo

class AttributeInline(admin.StackedInline):
    model = ProductAttribute

# assign photoInline to an andmin.ModelAdmin instance
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        PhotoInline,
    ]

# assign photoInline to an andmin.ModelAdmin instance
class ProductVariantAdmin(admin.ModelAdmin):
    inlines = [
        AttributeInline,
    ]

# Register your models here.
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
# attach admin inline rules to product class
admin.site.register(Photo)
admin.site.register(ProductVariant, ProductVariantAdmin)
