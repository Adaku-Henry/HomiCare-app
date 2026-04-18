from rest_framework import serializers
from .models import SupportTicket, TicketMessage, TicketCategory


class TicketCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = TicketCategory
        fields = "__all__"


class TicketMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = TicketMessage
        fields = "__all__"


class SupportTicketSerializer(serializers.ModelSerializer):

    messages = TicketMessageSerializer(many=True, read_only=True)

    class Meta:
        model = SupportTicket
        fields = "__all__"