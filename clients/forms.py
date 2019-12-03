from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
  class Meta:
    model = Client
    fields = [
      'name',
      'email',
      'phone',
      'address',
      'age' 
    ]

    labels = {
      'name': 'Name',
      'email': 'Email',
      'phone': 'Phone',
      'address': 'Address',
      'age': 'Age',
    }
