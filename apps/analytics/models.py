from django.db import models
from django.contrib.auth import get_user_model

from apps.services.models import Service

User = get_user_model()

class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_bookings = models.IntegerField(default=0)
    completed_bookings = models.IntegerField(default=0)
    pending_bookings = models.IntegerField(default=0)
    total_spent = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    last_active = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} Activity"

class ServiceAnalytics(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    total_bookings = models.IntegerField(default=0)
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    average_rating = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.service.name} Analytics"

class RevenueAnalytics(models.Model):
    date = models.DateField(auto_now_add=True)
    total_revenue = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    successful_transactions = models.IntegerField(default=0)
    failed_transactions = models.IntegerField(default=0)

    def __str__(self):
        return f"Revenue {self.date}"