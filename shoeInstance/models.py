from django.db import models
from shoe.models import Shoe
from purchase.models import Purchase
# Create your models here.
class ShoeInstance(models.Model):
    """Model representing a specific copy of a shoe (i.e. that can be purchased from a )."""
    shoe = models.ForeignKey(Shoe,  on_delete = models.SET_NULL, null = True)
    us_size = models.FloatField(default = 0.0, null = True)
    eu_size = models.FloatField(default = 0.0, null = True)
    purchase = models.ForeignKey(Purchase, on_delete=models.SET_NULL, null = True)

    
    STATUS = (
        ('R', 'Returned'),
        ('P', 'Purchased'),
        ('A', 'Available')
    )

    status = models.CharField(
        max_length=1,
        choices= STATUS,
        blank=True,
        default='A',
        help_text='Shoe availability')

    def __str__(self):
        """String for representing the Model object."""
        return '{0} ({1})'.format(self.shoe.name, self.status)