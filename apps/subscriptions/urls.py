from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    SubscriptionPlanViewSet,
    UserSubscriptionViewSet,
    PromoCodeViewSet
)

router = DefaultRouter()

router.register("plans", SubscriptionPlanViewSet)
router.register("subscriptions", UserSubscriptionViewSet)
router.register("promocodes", PromoCodeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]