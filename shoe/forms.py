from django import forms
from .models import Shoe

class ShoeForm(forms.ModelForm):
  class Meta:
    model = Shoe
    fields = [
      'type',
      'price',
      'height',
      'description',
      'color',
      'image_route',
      'release_date',
      'name',
      'supplier'
    ]

    labels = {
      'type' : 'Tipo',
      'price': 'Precio',
      'height': 'Altura',
      'description': 'Descripción',
      'color': 'Color',
      'image_route': 'Ruta Imagen',
      'release_date': 'Fecha Publicación',
      'name': 'Nombre',
      'supplier': 'Proveedor'
    }
