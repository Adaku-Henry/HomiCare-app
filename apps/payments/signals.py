from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Payment, UserSubscription

# Correct imports using apps/ prefix
from apps.analytics.services import update_user_activity, update_daily_revenue
try:
    from apps.notifications.services import send_notification
except ModuleNotFoundError:
    # fallback if notifications app is not ready yet
    def send_notification(user, message):
        pass

# --- Payment Signals ---
@receiver(post_save, sender=Payment)
def payment_signal(sender, instance, created, **kwargs):
    """
    Triggered whenever a Payment is created or updated.
    Updates Analytics and sends Notifications.
    """
    if created or instance.status in ['success', 'refunded', 'failed']:
        # Update analytics
        update_user_activity(instance.user)
        update_daily_revenue()

        # Send notification to user
        if instance.status == 'success':
            message = f"Your payment of {instance.amount} UGX was successful."
        elif instance.status == 'refunded':
            message = f"Your payment of {instance.amount} UGX has been refunded."
        elif instance.status == 'failed':
            message = f"Your payment of {instance.amount} UGX failed. Please try again."
        else:
            message = f"Your payment status changed to {instance.status}."

        send_notification(user=instance.user, message=message)


# --- Subscription Signals ---
@receiver(post_save, sender=UserSubscription)
def subscription_signal(sender, instance, created, **kwargs):
    """
    Triggered whenever a UserSubscription is created or updated.
    Sends notifications to user.
    """
    if created:
        message = f"You have successfully subscribed to {instance.plan.name}. " \
                  f"Your subscription will expire on {instance.end_date.strftime('%Y-%m-%d')}."
        send_notification(user=instance.user, message=message)
    else:
        if instance.status == 'expired':
            message = f"Your subscription to {instance.plan.name} has expired."
            send_notification(user=instance.user, message=message)
        elif instance.status == 'cancelled':
            message = f"Your subscription to {instance.plan.name} has been cancelled."
            send_notification(user=instance.user, message=message)