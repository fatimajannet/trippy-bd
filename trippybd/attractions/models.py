from django.db import models

class Attraction(models.Model):
    city = models.ForeignKey('cities.City', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    entry_fee = models.DecimalField(max_digits=6, decimal_places=2)
    opening_hours = models.CharField(max_length=100)

    def __str__(self):
        return self.name