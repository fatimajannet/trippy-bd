from django.db import models

# Create your models here.
from django.db import models

class Hotel(models.Model):
    city = models.ForeignKey('cities.City', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return self.name