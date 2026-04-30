from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Transportation

@admin.register(Transportation)
class TransportationAdmin(admin.ModelAdmin):
    # This makes the admin list view look professional
    list_display = ('t_id', 't_type', 'city', 'apprx_cost')
    list_filter = ('t_type', 'city') # Adds a filter sidebar
    search_fields = ('t_type', 't_desc')