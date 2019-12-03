from django.db import models

# Create your models here.

class Client(models.Model):
    """
        A class that defines all registered users in Antüsü's business
    """

    # Primitive Fields
    name = models.CharField(max_length = 50)
    age = models.IntegerField(default = 0)
    email = models.CharField(max_length = 50, default = "NR")
    phone = models.CharField(max_length = 20, default = "NR")
    address = models.CharField(max_length = 40, default = "NR")

    # One to many relationships to: purchase, 
    
    # Relationship Fields

    # Constraints
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'email'], name='antusu_user'),
            models.CheckConstraint(check=models.Q(age__gte=0), name='positive_age')
        ]

    #Methods

    def __str__(self):
        " String for representing the object"
        return "{}".format(self.nombre)
