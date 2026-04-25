from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TravelHistory


@admin.register(TravelHistory)
class TravelHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'visited_at')
    list_filter = ('visited_at',)
    search_fields = ('user__username', 'city__name')
    ordering = ('-visited_at',)
    date_hierarchy = 'visited_at'