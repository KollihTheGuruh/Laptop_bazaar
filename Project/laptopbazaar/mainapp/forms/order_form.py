from django import forms
from mainapp.models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'laptop', 'quantity']  # Specify the fields you need
