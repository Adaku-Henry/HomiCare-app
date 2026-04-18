from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Review
from apps.notifications.services import send_notification


@receiver(post_save, sender=Review)
def notify_provider_review(sender, instance, created, **kwargs):

    if created:

        provider_user = instance.provider.user

        send_notification(
            provider_user,
            "You have received a new review from a customer."
        )