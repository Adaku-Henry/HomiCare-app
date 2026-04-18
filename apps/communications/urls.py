from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .africastalking_client import ussd_callback
from .views import (
    ConversationViewSet, MessageViewSet,
    CallLogViewSet, NotificationViewSet
)

router = DefaultRouter()
router.register(r'conversations', ConversationViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'call-logs', CallLogViewSet)
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('ussd/', ussd_callback),
]