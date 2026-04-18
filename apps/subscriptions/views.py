from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import SubscriptionPlan, UserSubscription, PromoCode
from .serializers import (
    SubscriptionPlanSerializer,
    UserSubscriptionSerializer,
    PromoCodeSerializer
)


class SubscriptionPlanViewSet(viewsets.ModelViewSet):

    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer
    permission_classes = [IsAuthenticated]


class UserSubscriptionViewSet(viewsets.ModelViewSet):

    queryset = UserSubscription.objects.all()
    serializer_class = UserSubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        serializer.save(user=self.request.user)


class PromoCodeViewSet(viewsets.ModelViewSet):

    queryset = PromoCode.objects.all()
    serializer_class = PromoCodeSerializer
    permission_classes = [IsAuthenticated]