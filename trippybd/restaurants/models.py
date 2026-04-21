from django.db import models
from cities.models import City

class Restaurant(models.Model):
    city          = models.ForeignKey(City, on_delete=models.CASCADE)
    name          = models.CharField(max_length=200)
    description   = models.TextField()
    cuisine_type  = models.CharField(max_length=100)
    average_price = models.DecimalField(max_digits=8, decimal_places=2)
    rating        = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.name