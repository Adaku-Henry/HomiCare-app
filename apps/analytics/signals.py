from django.db.models.signals import post_save
from django.dispatch import receiver
from bookings.models import Booking
from payments.models import Payment
from .services import update_user_activity, update_service_analytics, update_daily_revenue

@receiver(post_save, sender=Booking)
def booking_analytics(sender, instance, created, **kwargs):
    if created:
        update_user_activity(instance.user)
        update_service_analytics(instance.service)

@receiver(post_save, sender=Payment)
def payment_analytics(sender, instance, created, **kwargs):
    if created and instance.status == 'success':
        update_user_activity(instance.user)
        update_service_analytics(instance.booking.service)
        update_daily_revenue()