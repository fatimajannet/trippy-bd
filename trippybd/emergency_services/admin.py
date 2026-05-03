from django.contrib import admin
from .models import EmergencyService

class EmergencyServiceInline(admin.TabularInline):
    model = EmergencyService
    extra = 1 

