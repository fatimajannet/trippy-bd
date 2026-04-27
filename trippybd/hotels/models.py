from django.db import models

class Amenity(models.Model):
    """
    Extracted from the multi-valued 'amenities' attribute (double oval).
    This allows a hotel to have multiple amenities, and multiple hotels to share the same amenity.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Hotel(models.Model):
    city = models.ForeignKey('cities.City', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    amenities = models.ManyToManyField(Amenity, related_name='hotels', blank=True)
    
    def __str__(self):
        return self.name

class Room(models.Model):
    # Hotel_has relationship: 1 to N mapping (ForeignKey)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    
    # r_id: Using CharField assuming it might be alphanumeric (e.g., "101A")
    r_id = models.CharField(max_length=50) 
    
    # Other room attributes
    r_type = models.CharField(max_length=100)
    r_price = models.DecimalField(max_digits=10, decimal_places=2)
    feature = models.TextField(blank=True, help_text="Specific room features or description")

    class Meta:
        # Enforcing the weak entity logic: r_id is unique ONLY within its specific hotel.
        constraints = [
            models.UniqueConstraint(fields=['hotel', 'r_id'], name='unique_hotel_room_id')
        ]

    def __str__(self):
        # FIXED: Changed self.hotel.h_name to self.hotel.name
        return f"{self.hotel.name} - Room {self.r_id} ({self.r_type})"
    

from django.conf import settings # To link to the logged-in user

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    check_in = models.DateField()
    check_out = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['room', 'check_in'], 
                name='unique_room_booking_per_day'
            )
        ]
    def __str__(self):
        return f"{self.user.username} - {self.room.hotel.name} ({self.check_in})"