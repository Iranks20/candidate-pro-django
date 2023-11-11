# forms.py

from django import forms
from .models import Subscriber
from .models import CheckoutOrder

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = CheckoutOrder
        fields = ['first_name', 'last_name', 'company_name', 'address', 'town_city', 'phone', 'email', 'order_notes', 'product_name', 'size', 'quantity', 'unit_cost', 'delivery_cost', 'total_cost']

