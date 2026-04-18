from django.db import models
from django.contrib.auth import get_user_model
from apps.providers.models import ProviderProfile
from apps.services.models import Service

User = get_user_model()

class Booking(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
        ('DECLINED', 'Declined'),
    ]

    RECURRING_CHOICES = [
        ('NONE', 'None'),
        ('DAILY', 'Daily'),
        ('WEEKLY', 'Weekly'),
        ('MONTHLY', 'Monthly'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    provider = models.ForeignKey(ProviderProfile, on_delete=models.CASCADE, related_name='provider_bookings')
    services = models.ManyToManyField(Service, related_name='booking_services')  # Multiple services
    booking_date = models.DateField()
    booking_time = models.TimeField()
    location = models.CharField(max_length=255)
    notes = models.TextField(blank=True)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    recurring = models.CharField(max_length=10, choices=RECURRING_CHOICES, default='NONE')
    emergency = models.BooleanField(default=False)  # Instant booking
    reference = models.CharField(max_length=50, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.reference or self.id} - {self.user.username}"

    def save(self, *args, **kwargs):
        if not self.reference:
            self.reference = f"HC-{self.user.id}-{self.booking_date.strftime('%Y%m%d')}-{self.id or 'NEW'}"
        super().save(*args, **kwargs)

class BookingAttachment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='attachments')
    image = models.ImageField(upload_to='booking_photos/')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Attachment {self.id} for {self.booking.reference}"

class BookingRating(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='rating')
    rating = models.PositiveIntegerField(default=5)
    review = models.TextField(blank=True)

    def __str__(self):
        return f"Rating for {self.booking.reference} - {self.rating}"