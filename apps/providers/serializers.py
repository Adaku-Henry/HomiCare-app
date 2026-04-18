from rest_framework import serializers
from .models import (
    ProviderProfile,
    ProviderService,
    ProviderAvailability,
    ProviderReview
)


class ProviderProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProviderProfile
        fields = "__all__"


class ProviderServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProviderService
        fields = "__all__"


class ProviderAvailabilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProviderAvailability
        fields = "__all__"


class ProviderReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProviderReview
        fields = "__all__"