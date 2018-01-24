from django import forms
from django.forms import ModelForm	
from django_countries.fields import LazyTypedChoiceField
from django.core.exceptions import ValidationError 
from django.core import validators
from django_countries import countries
import re

def validate_alphanumeric(value):
	"""
	check postcode form fields for non-alphanumeric characters or dashes or underscores
	"""
	if not re.search('^[0-9a-zA-Z_-]+\Z', value):
		raise forms.ValidationError("Postcode must only contain letters or numbers")
	else:
		return value

class OrderForm(forms.Form):

	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)
	email = forms.EmailField()
	address1 = forms.CharField(max_length=100, label='Address')
	town = forms.CharField(max_length=100)
	postcode = forms.CharField(validators=[validate_alphanumeric])
	country = LazyTypedChoiceField(choices=countries)
	additional_note = forms.CharField(max_length=100, required=False)