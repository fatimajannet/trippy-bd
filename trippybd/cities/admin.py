from django.contrib import admin
from .models import City

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display  = ('name', 'region', 'population')
    list_filter   = ('region',)
    search_fields = ('name', 'region')
    ordering      = ('name',)