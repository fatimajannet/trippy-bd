from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    population = models.IntegerField()
    region = models.CharField(max_length=100)

    def __str__(self):
        return self.name