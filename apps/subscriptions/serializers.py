from rest_framework import serializers
from .models import SubscriptionPlan, UserSubscription, PromoCode


class SubscriptionPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubscriptionPlan
        fields = "__all__"


class UserSubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserSubscription
        fields = "__all__"


class PromoCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PromoCode
        fields = "__all__"