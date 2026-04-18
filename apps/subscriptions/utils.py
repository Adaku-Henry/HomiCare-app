from django.utils.timezone import now


def subscription_expiring(subscription):

    remaining = subscription.end_date - now()

    return remaining.days <= 3