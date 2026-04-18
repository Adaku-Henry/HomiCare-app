from django.urls import path
from .views import UserActivityView, ServiceAnalyticsView, RevenueAnalyticsView

urlpatterns = [
    path('user-activity/', UserActivityView.as_view(), name='user-activity'),
    path('services/', ServiceAnalyticsView.as_view(), name='service-analytics'),
    path('revenue/', RevenueAnalyticsView.as_view(), name='revenue-analytics'),
]