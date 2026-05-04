from django.contrib import admin
from .models import Transportation

@admin.register(Transportation)
class TransportationAdmin(admin.ModelAdmin):
    list_display = ('t_id', 't_type', 'city', 'apprx_cost')
    list_filter = ('t_type', 'city') 
    search_fields = ('t_type', 't_desc')