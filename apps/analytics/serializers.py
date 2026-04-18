from rest_framework import serializers
from .models import UserActivity, ServiceAnalytics, RevenueAnalytics

class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActivity
        fields = [
            "user",
            "total_bookings",
            "completed_bookings",
            "pending_bookings",
            "total_spent",
            "last_active"
        ]
        read_only_fields = fields

class ServiceAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceAnalytics
        fields = [
            "service",
            "total_bookings",
            "total_revenue",
            "average_rating"
        ]
        read_only_fields = fields

class RevenueAnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueAnalytics
        fields = [
            "date",
            "total_revenue",
            "successful_transactions",
            "failed_transactions"
        ]
        read_only_fields = fields