from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import TicketMessage
from apps.notifications.services import send_notification


@receiver(post_save, sender=TicketMessage)
def notify_ticket_reply(sender, instance, created, **kwargs):

    if created:

        user = instance.ticket.user

        send_notification(
            user,
            "Your support ticket has a new reply."
        )