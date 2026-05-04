from django.db import models
from django.conf import settings

class Agency(models.Model):
    city = models.ForeignKey('cities.City', on_delete=models.CASCADE, related_name='agencies')
    ag_id = models.CharField(max_length=50, unique=True)
    ag_name = models.CharField(max_length=150)
    ag_rating = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return self.ag_name

class Guide(models.Model):
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, related_name='guides')
    g_id = models.CharField(max_length=50, unique=True)
    g_name = models.CharField(max_length=150)
    g_rating = models.DecimalField(max_digits=2, decimal_places=1)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.g_name

class GuideHire(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE)
    hire_date = models.DateField()
    days = models.PositiveIntegerField(default=1)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='Confirmed')
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['guide', 'hire_date'], 
                name='unique_guide_booking_per_day'
            )
        ]
    def __str__(self):
        return f"{self.user.username} hired {self.guide.g_name}"