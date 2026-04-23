from django.db import models
from django.conf import settings
from cities.models import City   # adjust import path if needed

class Wishlist(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='wishlist_items'
    )
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'city')
        ordering = ['-added_date']

    def __str__(self):
        return f"{self.user.username} - {self.city.name}"