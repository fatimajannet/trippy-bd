from django.db import models
from django.conf import settings
from cities.models import City  


class TravelHistory(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='travel_history'
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='visited_by'
    )
    visited_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-visited_at']
        unique_together = ('user', 'city')
        verbose_name = 'Travel History'
        verbose_name_plural = 'Travel Histories'

    def __str__(self):
        return f"{self.user.username} visited {self.city.name} on {self.visited_at.strftime('%Y-%m-%d')}"