from django import forms
from django.forms import ModelForm
from products.models import ProductAttribute	
from django_countries.fields import LazyTypedChoiceField
from django.core.exceptions import ValidationError 
from django.core import validators
from django_countries import countries
import re


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 20)]

class CartAddProductForm(forms.Form):

	quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,
		coerce=int)
	update_quantity = forms.BooleanField(required=False,
		initial=False,widget=forms.HiddenInput)
	update_variant = forms.BooleanField(required=False,
	initial=False,widget=forms.HiddenInput)
	variant = forms.ModelChoiceField(queryset=ProductAttribute.objects.filter(),required=False, empty_label=None,)

