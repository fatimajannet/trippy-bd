from django.db import models
from cities.models import City  

class EmergencyService(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='emergency_services')
    
    es_name = models.CharField(max_length=200, help_text="Service Name (e.g., City General Hospital)")
    es_contact = models.CharField(max_length=100, help_text="Contact Numbers")
    
    def __str__(self):
        return f"{self.es_name} - {self.city.name}"