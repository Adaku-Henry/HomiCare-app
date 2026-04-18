from .services import update_user_activity, update_service_analytics, update_daily_revenue
from django.contrib.auth import get_user_model
from services.models import Service


def refresh_all_analytics():
    """
    Refresh all analytics for users, services, and revenue.
    Can be scheduled with a cron job or Celery for periodic updates.
    """

    User = get_user_model()
    for user in User.objects.all():
        update_user_activity(user)

    for service in Service.objects.all():
        update_service_analytics(service)

    update_daily_revenue()