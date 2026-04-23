from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Wishlist

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'added_date')
    search_fields = ('user__username', 'city__name')
    readonly_fields = ('added_date',)