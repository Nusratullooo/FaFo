from django import forms

from home.models import ContactMessage
from product.models import Order


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ('name', 'email', 'phone', 'subject', 'message')


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('food', 'price', 'name', 'address', 'amount')
