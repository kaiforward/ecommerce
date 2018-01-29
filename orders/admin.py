import csv
import datetime
from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse
# use makr safe instead of allow_tags in django2.0
from django.utils.safestring import mark_safe
from .models import CustomerOrder, CustomerProduct, Shipping, ShippingChoice

def export_to_csv(modeladmin, request, queryset):
	opts = modeladmin.model._meta
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attatchment; filename={}.csv'.format(opts.verbose_name)
	writer = csv.writer(response)

	fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
	# write the header row
	writer.writerow([field.verbose_name for field in fields])
	# write data rows
	for obj in queryset:
		data_row = []
		for field in fields:
			value = getattr(obj, field.name)
			if isinstance(value, datetime.datetime):
				value = value.strftime('%d%m%y')
			data_row.append(value)
		writer.writerow(data_row)
	return response

export_to_csv.short_description = 'Export to CSV'	

def order_detail(obj):
	return mark_safe('<a href="{}">View</a>'.format(reverse('admin_order_detail', args=[obj.pk])))

# Register your models here.
class OrderInline(admin.TabularInline):
	model = CustomerProduct
	raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
	list_display = ['pk', order_detail, 'first_name', 'last_name', 'email', 'address1', 'post_code', 'town', 'country', 'date_created', 'paid']
	list_filter = ['paid', 'date_created', 'date_updated']
	inlines = [OrderInline]
	actions = [export_to_csv]

class ShippingInline(admin.StackedInline):
	model = ShippingChoice

class ShippingAdmin(admin.ModelAdmin):
	inlines = [ShippingInline]

admin.site.register(CustomerOrder, OrderAdmin)
admin.site.register(Shipping, ShippingAdmin)