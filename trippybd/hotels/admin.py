from django.contrib import admin
from .models import Hotel, Room, Amenity, Booking

admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Amenity)
admin.site.register(Booking)