from django import forms
from .models import ShoeInstance

class ShoeInstanceForm(forms.ModelForm):
  class Meta:
    model = ShoeInstance
    fields = [
      'shoe',
      'us_size',
      'eu_size',
      'purchase'
    ]

    labels = {
      'shoe': 'Shoe',
      'us_size': 'US Size',
      'eu_size': 'EU Size',
      'purchase': 'Purchase'
    }
