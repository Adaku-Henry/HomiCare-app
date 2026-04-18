from datetime import timedelta
from django.utils.timezone import now

from .models import UserSubscription


def create_subscription(user, plan):

    start = now()

    if plan.billing_cycle == "monthly":
        end = start + timedelta(days=30)

    else:
        end = start + timedelta(days=365)

    subscription = UserSubscription.objects.create(
        user=user,
        plan=plan,
        start_date=start,
        end_date=end
    )

    return subscription


def cancel_subscription(subscription):

    subscription.status = "cancelled"
    subscription.auto_renew = False
    subscription.save()

    return subscription


def check_subscription_active(user):

    sub = UserSubscription.objects.filter(
        user=user,
        status="active"
    ).first()

    if not sub:
        return False

    if sub.end_date < now():

        sub.status = "expired"
        sub.save()

        return False

    return True