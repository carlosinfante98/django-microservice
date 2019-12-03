from django import forms
from .models import Purchase

class PurchaseForm(forms.ModelForm):
  class Meta:
    model = Purchase
    fields = [
      'owner',
      'total_price',
      'purchase_date',
      'delivery_date',
    ]

    labels = {
      'owner': 'Owner',
      'total_price': 'Total Price',
      'purchase_date': 'Purchase Date',
      'delivery_date': 'Delivery Date',
    }
