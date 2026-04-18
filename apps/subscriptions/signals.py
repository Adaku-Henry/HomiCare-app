from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UserSubscription
from apps.notifications.services import send_notification


@receiver(post_save, sender=UserSubscription)
def notify_subscription(sender, instance, created, **kwargs):

    if created:

        send_notification(
            instance.user,
            f"Your subscription to {instance.plan.name} is now active."
        )