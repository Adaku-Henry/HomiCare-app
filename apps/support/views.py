from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import SupportTicket, TicketMessage, TicketCategory
from .serializers import (
    SupportTicketSerializer,
    TicketMessageSerializer,
    TicketCategorySerializer
)


class TicketCategoryViewSet(viewsets.ModelViewSet):

    queryset = TicketCategory.objects.all()

    serializer_class = TicketCategorySerializer

    permission_classes = [IsAuthenticated]


class SupportTicketViewSet(viewsets.ModelViewSet):

    queryset = SupportTicket.objects.all()

    serializer_class = SupportTicketSerializer

    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        serializer.save(user=self.request.user)


class TicketMessageViewSet(viewsets.ModelViewSet):

    queryset = TicketMessage.objects.all()

    serializer_class = TicketMessageSerializer

    permission_classes = [IsAuthenticated]