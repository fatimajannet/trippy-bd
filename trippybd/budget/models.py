from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from cities.models import City

class BudgetPlan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    days = models.PositiveIntegerField(default=1)
    
    # These are the "selected" values for the saved plan
    tier_selected = models.CharField(max_length=20, choices=[
        ('budget', 'Budget'),
        ('standard', 'Standard'),
        ('premium', 'Premium')
    ])
    
    total_estimated_cost = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s plan for {self.city.name}"