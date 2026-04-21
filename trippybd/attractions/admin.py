from django.contrib import admin
from .models import Attraction

@admin.register(Attraction)
class AttractionAdmin(admin.ModelAdmin):
    list_display  = ('name', 'city', 'entry_fee', 'opening_hours')
    list_filter   = ('city',)
    search_fields = ('name', 'description')
    ordering      = ('city', 'name')