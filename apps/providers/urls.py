from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    ProviderProfileViewSet,
    ProviderServiceViewSet,
    ProviderAvailabilityViewSet,
    ProviderReviewViewSet
)

router = DefaultRouter()

router.register("profiles", ProviderProfileViewSet)
router.register("services", ProviderServiceViewSet)
router.register("availability", ProviderAvailabilityViewSet)
router.register("reviews", ProviderReviewViewSet)

urlpatterns = [
    path("", include(router.urls)),
]