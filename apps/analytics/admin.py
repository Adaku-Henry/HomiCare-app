from django.contrib import admin
from .models import UserActivity, ServiceAnalytics, RevenueAnalytics

@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    list_display = ("user", "total_bookings", "completed_bookings", "pending_bookings", "total_spent", "last_active")
    search_fields = ("user__username",)

@admin.register(ServiceAnalytics)
class ServiceAnalyticsAdmin(admin.ModelAdmin):
    list_display = ("service", "total_bookings", "total_revenue", "average_rating")
    search_fields = ("service__name",)

@admin.register(RevenueAnalytics)
class RevenueAnalyticsAdmin(admin.ModelAdmin):
    list_display = ("date", "total_revenue", "successful_transactions", "failed_transactions")
    list_filter = ("date",)