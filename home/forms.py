from django import forms
from django.db import models
from django.forms import fields
from django.forms.widgets import CheckboxInput
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

from .models import Category, Product


# PAYMENT_CHOICES = (
    
#     ('S','Stripe'),
#     ('P','PayPAl')
# )

# class CheckoutForm(forms.Form):
#     street_address       = forms.CharField()
#     apartment_address    = forms.CharField()
#     country              = CountryField(blank_label='(Select country)').formfield(widget=CountrySelectWidget)
#     zip                  = forms.CharField()
#     same_shipping_address = forms.BooleanField(widget=forms.CheckboxInput())
#     save_info            = forms.BooleanField(widget=forms.CheckboxInput())
#     payment_option       = forms.ChoiceField(
#                             widget=forms.RadioSelect, choices=PAYMENT_CHOICES)
    
    
    
class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'price', 'category', 'discount_price', 'description']
        
class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
    