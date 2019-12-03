from django import forms
from .models import Supplier

class SupplierForm(forms.ModelForm):
  class Meta:
    model = Supplier
    fields =[
      'name',
      'email',
      'phone',
      'nit',
      'city',
      'address',
    ]

    labels = {
      'name': 'Nombre',
      'email': 'E-Mail',
      'phone': 'Teléfono',
      'nit': 'NIT',
      'city': 'Ciudad',
      'address': 'Dirección',
    }