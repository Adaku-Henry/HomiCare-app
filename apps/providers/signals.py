from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ProviderReview
from .services import update_provider_rating


@receiver(post_save, sender=ProviderReview)
def update_rating(sender, instance, created, **kwargs):

    if created:
        update_provider_rating(instance.provider)