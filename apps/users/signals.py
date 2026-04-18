from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User, ActivityLog


@receiver(post_save, sender=User)
def log_user_activity(sender, instance, created, **kwargs):

    if created:
        action = "User Created"
    else:
        action = "User Updated"

    ActivityLog.objects.create(
        user=instance,
        action=action,
        details=f"User {instance.username} saved."
    )