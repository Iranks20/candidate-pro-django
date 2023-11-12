# forms.py

from django import forms
from .models import Subscriber
from .models import CheckoutOrder

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']

