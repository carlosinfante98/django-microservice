from django.db import models
from clients.models import Client

# Create your models here.
class Purchase(models.Model):
  owner = models.ForeignKey(Client, on_delete = models.SET_NULL, null = True)
  total_price = models.FloatField(default=0.0)
  purchase_date = models.DateTimeField('date purchased', null = True)
  delivery_date = models.DateTimeField('delivery date', null = True)

  # Model constraints
  class Meta:
    constraints = [
      models.CheckConstraint(
        check=models.Q(total_price__gte=0),
        name= 'positive_price'
      ),

      models.UniqueConstraint(
        fields=['owner', 'purchase_date'],
        name='unique_purchase_owner'
      )
    ]

    