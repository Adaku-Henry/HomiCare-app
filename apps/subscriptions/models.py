from django.db import models
from django.conf import settings
from django.utils.timezone import now

User = settings.AUTH_USER_MODEL


class SubscriptionPlan(models.Model):

    BILLING_CHOICES = (
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
    )

    name = models.CharField(max_length=100)
    description = models.TextField()

    price = models.DecimalField(max_digits=10, decimal_places=2)

    billing_cycle = models.CharField(
        max_length=20,
        choices=BILLING_CHOICES
    )

    trial_days = models.IntegerField(default=0)

    max_bookings = models.IntegerField(default=0)
    priority_support = models.BooleanField(default=False)
    featured_listing = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class UserSubscription(models.Model):

    STATUS_CHOICES = (
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscriptions'
    )

    plan = models.ForeignKey(
        SubscriptionPlan,
        on_delete=models.CASCADE
    )

    start_date = models.DateTimeField(default=now)
    end_date = models.DateTimeField()

    auto_renew = models.BooleanField(default=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.plan}"
    
class PromoCode(models.Model):

    code = models.CharField(max_length=50, unique=True)

    discount_percent = models.IntegerField()

    max_usage = models.IntegerField(default=100)

    used_count = models.IntegerField(default=0)

    expires_at = models.DateTimeField()

    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code