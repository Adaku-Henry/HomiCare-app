from django.urls import path
from .views import BookingPaymentView, SubscribeView, RefundPaymentView, SubscriptionPlanListView

urlpatterns = [
    path('pay/', BookingPaymentView.as_view(), name='booking-pay'),
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
    path('refund/', RefundPaymentView.as_view(), name='refund-payment'),
    path('plans/', SubscriptionPlanListView.as_view(), name='subscription-plans'),
]