from django.contrib.auth.models import User
from django import forms
from .models import *

class InitialForm(forms.Form):
	phone = forms.IntegerField(widget=forms.TextInput(),min_value=6000000000)
	secret_pin = forms.IntegerField(widget=forms.PasswordInput(), max_value=999999)

class OrderForm(forms.Form):
	item1 = forms.CharField(required=False, initial = "")
	quantity1 = forms.IntegerField(widget=forms.TextInput(), required=False, initial = 0, min_value = 0)
	item2 = forms.CharField(required=False, initial = "")
	quantity2 = forms.IntegerField(widget=forms.TextInput(), required=False, initial = 0, min_value = 0)
	item3 = forms.CharField(required=False, initial = "")
	quantity3 = forms.IntegerField(widget=forms.TextInput(), required=False, initial = 0, min_value = 0)
	item4 = forms.CharField(required=False, initial = "")
	quantity4 = forms.IntegerField(widget=forms.TextInput(), required=False, initial = 0, min_value = 0)
	item5 = forms.CharField(required=False, initial = "")
	quantity5 = forms.IntegerField(widget=forms.TextInput(), required=False, initial = 0, min_value = 0)

class CancelForm(forms.Form):
	ref_no = forms.IntegerField(widget = forms.TextInput(), max_value = 999999)
	secret_pin = forms.IntegerField(widget = forms.PasswordInput(), max_value = 999999)

class PrintForm(forms.Form):
	ref_no = forms.IntegerField(widget = forms.TextInput(), max_value = 999999)
	secret_pin = forms.IntegerField(widget = forms.PasswordInput(), max_value = 999999)