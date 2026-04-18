from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, ActivityLog


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = (
        'username',
        'email',
        'phone_number',
        'user_type',
        'is_active'
    )

    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': (
                'phone_number',
                'is_verified',
                'user_type'
            )
        }),
    )


@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):

    list_display = ('user', 'action', 'timestamp')

    search_fields = ('user__username', 'action')

    list_filter = ('timestamp',)