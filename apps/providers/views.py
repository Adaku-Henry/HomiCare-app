from rest_framework import viewsets
from .models import (
    ProviderProfile,
    ProviderService,
    ProviderAvailability,
    ProviderReview
)

from .serializers import (
    ProviderProfileSerializer,
    ProviderServiceSerializer,
    ProviderAvailabilitySerializer,
    ProviderReviewSerializer
)


class ProviderProfileViewSet(viewsets.ModelViewSet):

    queryset = ProviderProfile.objects.all()

    serializer_class = ProviderProfileSerializer


class ProviderServiceViewSet(viewsets.ModelViewSet):

    queryset = ProviderService.objects.all()

    serializer_class = ProviderServiceSerializer


class ProviderAvailabilityViewSet(viewsets.ModelViewSet):

    queryset = ProviderAvailability.objects.all()

    serializer_class = ProviderAvailabilitySerializer


class ProviderReviewViewSet(viewsets.ModelViewSet):

    queryset = ProviderReview.objects.all()

    serializer_class = ProviderReviewSerializer