
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    list_display  = ('username', 'email', 'fname', 'lname', 'u_location', 'is_staff')
    search_fields = ('username', 'email', 'fname', 'lname')
    ordering      = ('username',)

    fieldsets = (
        (None,            {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('fname', 'mname', 'lname', 'email', 'u_location')}),
        ('Permissions',   {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Dates',         {'fields': ('date_joined',)}),
    )
    readonly_fields = ('date_joined', 'u_id')

admin.site.register(User, UserAdmin)



