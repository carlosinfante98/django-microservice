from django.db import models

# Create your models here.
class Supplier(models.Model):
  name = models.CharField(max_length=250)
  email = models.CharField(max_length=250)
  phone = models.CharField(max_length=250)
  nit = models.CharField(max_length=250)
  city = models.CharField(max_length=250)
  address = models.CharField(max_length=250)

  def __str__(self):
    return "{}".format(self.name)

