from django.db import models
from suppliers.models import Supplier

# Create your models here.
class Shoe (models.Model):
  name = models.CharField(max_length = 40, default = "__", null = True)
  release_date = models.DateTimeField('release date', null = True)
  price = models.FloatField(default = 0.0, null = True)
  supplier = models.ForeignKey(Supplier, null = True, on_delete = models.CASCADE)
  description = models.CharField(max_length = 40, null = True)
  type = models.CharField(max_length = 40, null = True)
  height = models.FloatField(default = 0.0, null = True)
  color = models.CharField(max_length = 20, null = True)
  image_route = models.CharField(max_length = 2000, default = "blank.png", null = True)

  def __str__(self):
    return "{},{},{},{}".format(self.name,self.supplier, self.release_date, self.price)