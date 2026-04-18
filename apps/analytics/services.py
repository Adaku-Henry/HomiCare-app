from .models import UserActivity, ServiceAnalytics, RevenueAnalytics
from apps.bookings.models import Booking
from apps.payments.models import Payment
from django.db.models import Sum, Count, Avg
from django.utils.timezone import now

# --- USER ACTIVITY ---
def update_user_activity(user):
    bookings = Booking.objects.filter(user=user)
    completed = bookings.filter(status='completed').count()
    pending = bookings.filter(status='pending').count()
    total_spent = Payment.objects.filter(user=user, status='success').aggregate(Sum('amount'))['amount__sum'] or 0

    activity, _ = UserActivity.objects.get_or_create(user=user)
    activity.total_bookings = bookings.count()
    activity.completed_bookings = completed
    activity.pending_bookings = pending
    activity.total_spent = total_spent
    activity.save()
    return activity

# --- SERVICE ANALYTICS ---
def update_service_analytics(service):
    bookings = Booking.objects.filter(service=service, status='completed')
    revenue = Payment.objects.filter(booking__service=service, status='success').aggregate(Sum('amount'))['amount__sum'] or 0
    # Calculate average rating assuming Service model has a related 'ratings' field
    avg_rating = service.ratings.aggregate(Avg('rating'))['rating__avg'] or 0

    analytics, _ = ServiceAnalytics.objects.get_or_create(service=service)
    analytics.total_bookings = bookings.count()
    analytics.total_revenue = revenue
    analytics.average_rating = avg_rating
    analytics.save()
    return analytics

# --- DAILY REVENUE ---
def update_daily_revenue():
    today = now().date()
    payments = Payment.objects.filter(date__date=today)
    total_revenue = payments.filter(status='success').aggregate(Sum('amount'))['amount__sum'] or 0
    successful = payments.filter(status='success').count()
    failed = payments.filter(status='failed').count()

    revenue, _ = RevenueAnalytics.objects.get_or_create(date=today)
    revenue.total_revenue = total_revenue
    revenue.successful_transactions = successful
    revenue.failed_transactions = failed
    revenue.save()
    return revenue