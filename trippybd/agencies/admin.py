from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Agency, Guide, GuideHire

@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_display = ('ag_name', 'city', 'ag_rating')

@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = ('g_name', 'agency', 'g_rating', 'price_per_day')



@admin.register(GuideHire)
class GuideHireAdmin(admin.ModelAdmin):
    list_display = ('user', 'guide', 'hire_date', 'status', 'total_cost')
    list_filter = ('status', 'hire_date')
    search_fields = ('user__username', 'guide__g_name')
    list_editable = ('status',) # Allows you to change status directly from the list view!