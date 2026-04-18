from django.db import models
from django.contrib.auth import get_user_model
from apps.services.models import Service

User = get_user_model()


class ProviderProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_photo = models.ImageField(upload_to="providers/photos/", blank=True)

    phone_number = models.CharField(max_length=20)

    location = models.CharField(max_length=200)

    national_id = models.CharField(max_length=50, blank=True)

    experience_years = models.IntegerField(default=0)

    bio = models.TextField(blank=True)

    skills = models.TextField(blank=True)

    is_verified = models.BooleanField(default=False)

    rating = models.FloatField(default=0)

    total_reviews = models.IntegerField(default=0)

    jobs_completed = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class ProviderService(models.Model):

    provider = models.ForeignKey(
        ProviderProfile,
        on_delete=models.CASCADE,
        related_name="services"
    )

    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE
    )

    price = models.DecimalField(max_digits=10, decimal_places=2)

    description = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.provider} - {self.service}"


class ProviderPortfolio(models.Model):

    provider = models.ForeignKey(
        ProviderProfile,
        on_delete=models.CASCADE,
        related_name="portfolio"
    )

    image = models.ImageField(upload_to="providers/portfolio/")

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.provider} Portfolio"


class ProviderAvailability(models.Model):

    provider = models.ForeignKey(
        ProviderProfile,
        on_delete=models.CASCADE,
        related_name="availability"
    )

    day_of_week = models.CharField(max_length=20)

    start_time = models.TimeField()

    end_time = models.TimeField()

    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.provider} - {self.day_of_week}"


class ProviderVerification(models.Model):

    provider = models.OneToOneField(
        ProviderProfile,
        on_delete=models.CASCADE
    )

    national_id_document = models.FileField(upload_to="providers/documents/")

    certificate = models.FileField(upload_to="providers/certificates/", blank=True)

    police_clearance = models.FileField(upload_to="providers/clearance/", blank=True)

    verified = models.BooleanField(default=False)

    verified_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.provider} verification"


class ProviderReview(models.Model):

    provider = models.ForeignKey(
        ProviderProfile,
        on_delete=models.CASCADE,
        related_name="provider_reviews"
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    rating = models.IntegerField()

    comment = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.provider} - {self.rating}"


class ProviderNotification(models.Model):

    provider = models.ForeignKey(
        ProviderProfile,
        on_delete=models.CASCADE,
        related_name="notifications"
    )

    title = models.CharField(max_length=200)

    message = models.TextField()

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.provider} Notification"