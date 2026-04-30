from django.db import models

# Create your models here.
from django.db import models

class Transportation(models.Model):
    t_id = models.AutoField(primary_key=True)
    t_type = models.CharField(max_length=50)
    t_desc = models.TextField()
    apprx_cost = models.DecimalField(max_digits=10, decimal_places=2)
    
    city = models.ForeignKey('cities.City', on_delete=models.CASCADE, related_name='transportations')

    def __str__(self):
        return f"{self.t_type} in {self.city.name}"