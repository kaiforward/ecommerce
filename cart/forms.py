from django import forms
from django.forms import ModelForm
from products.models import Product, ProductVariant, ProductAttribute	


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 20)]

class CartAddProductForm(forms.Form):

	quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,
		coerce=int)

	update_quantity = forms.BooleanField(required=False,
		initial=False,widget=forms.HiddenInput)

	update_variant = forms.BooleanField(required=False,
	initial=False,widget=forms.HiddenInput)

	variant = forms.ModelChoiceField(queryset=ProductAttribute.objects.filter())