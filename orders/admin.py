from django.contrib import admin
from .models import CustomerOrder, CustomerProduct

# Register your models here.
class OrderInline(admin.TabularInline):
	model = CustomerProduct
	raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
	list_display = ['pk', 'first_name', 'last_name', 'email', 'address1', 'post_code', 'town', 'country',]
	list_filter = ['paid', 'date_created', 'date_updated']
	inlines = [OrderInline]

admin.site.register(CustomerOrder, OrderAdmin)