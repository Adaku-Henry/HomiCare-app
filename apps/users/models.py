from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):

    phone_number = models.CharField(max_length=15, blank=True, null=True)

    is_verified = models.BooleanField(default=False)

    USER_TYPES = (
        ('customer', 'Customer'),
        ('provider', 'Service Provider'),
        ('admin', 'Admin'),
    )

    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='customer')

    def __str__(self):
        return self.username


class ActivityLog(TimeStampedModel):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    action = models.CharField(max_length=255)

    details = models.TextField(blank=True)

    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user} - {self.action}"