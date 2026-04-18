from datetime import timedelta
from django.utils.timezone import now
import uuid

from .models import Payment, UserSubscription, SubscriptionPlan
from apps.analytics.services import update_user_activity, update_daily_revenue
from apps.notifications.services import send_notification  # Notifications service

# --- Generate a unique transaction ID ---
def generate_transaction_id():
    return str(uuid.uuid4())

# --- Process Payment for a Bookings ---
def process_booking_payment(user, booking, amount, payment_method='mobile_money'):
    """
    Creates a Payment record for a booking, updates analytics, and sends notifications.
    """
    payment = Payment.objects.create(
        user=user,
        booking=booking,
        amount=amount,
        payment_method=payment_method,
        transaction_id=generate_transaction_id(),
        status='success',  # For demo purposes; integrate real payment gateway
    )

    # Update analytics
    update_user_activity(user)
    update_daily_revenue()

    # Send notification
    send_notification(user=user, message=f"Your payment of {amount} UGX for the booking was successful.")

    return payment

# --- Subscribe User to a Plan ---
def subscribe_user(user, plan_id, payment_method='mobile_money'):
    """
    Processes subscription payment and creates UserSubscription record.
    """
    plan = SubscriptionPlan.objects.get(id=plan_id)

    # Create Payment
    payment = Payment.objects.create(
        user=user,
        amount=plan.price,
        payment_method=payment_method,
        transaction_id=generate_transaction_id(),
        status='success',  # Assume success for demo
    )

    # Create Subscription
    subscription = UserSubscription.objects.create(
        user=user,
        plan=plan,
        start_date=now(),
        end_date=now() + timedelta(days=plan.duration_days),
        status='active',
        transaction=payment
    )

    # Update analytics
    update_user_activity(user)
    update_daily_revenue()

    # Send notification
    send_notification(
        user=user,
        message=f"You have successfully subscribed to {plan.name}. Your subscription expires on {subscription.end_date.strftime('%Y-%m-%d')}."
    )

    return subscription, payment

# --- Refund Payment ---
def refund_payment(payment_id):
    """
    Refunds a payment, updates analytics, and sends notifications.
    """
    try:
        payment = Payment.objects.get(id=payment_id)
    except Payment.DoesNotExist:
        return None

    if payment.status == 'success':
        payment.status = 'refunded'
        payment.save()

        # Update analytics
        update_user_activity(payment.user)
        update_daily_revenue()

        # Send notification
        send_notification(
            user=payment.user,
            message=f"Your payment of {payment.amount} UGX has been refunded."
        )
        return payment

    return None