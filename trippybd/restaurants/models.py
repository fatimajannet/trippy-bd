from django.db import models

# Create your models here.
from django.db import models

class Restaurant(models.Model):
    city = models.ForeignKey('cities.City', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    cuisine_type = models.CharField(max_length=100)
    average_price = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return self.name
    

