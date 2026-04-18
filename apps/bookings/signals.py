from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Booking

@receiver(post_save, sender=Booking)
def booking_completed(sender, instance, **kwargs):
    if instance.status == "COMPLETED":
        provider = instance.provider
        provider.jobs_completed += 1
        provider.save()