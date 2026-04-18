from rest_framework import viewsets, permissions
from .models import Conversation, Message, CallLog, Notification
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


from .serializers import (
    ConversationSerializer, MessageSerializer,
    CallLogSerializer, NotificationSerializer
)

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class CallLogViewSet(viewsets.ModelViewSet):
    queryset = CallLog.objects.all()
    serializer_class = CallLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(caller=self.request.user)


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]


@csrf_exempt
def ussd_callback(request):

    session_id = request.POST.get('sessionId')
    phone_number = request.POST.get('phoneNumber')
    text = request.POST.get('text')

    # MAIN MENU
    if text == '':
        response = "CON Welcome to HomiCare\n"
        response += "1. Book a Service\n"
        response += "2. My Appointments\n"
        response += "3. Customer Support"

    # BOOK SERVICE
    elif text == '1':
        response = "CON Choose Service Category\n"
        response += "1. Cleaning Services\n"
        response += "2. Plumbing Services\n"
        response += "3. Electrical Services\n"
        response += "4. Building & Repairs\n"
        response += "5. Home Care Services"

    # CLEANING SERVICES
    elif text == '1*1':
        response = "CON Cleaning Services\n"
        response += "1. House Cleaning\n"
        response += "2. Office Cleaning\n"
        response += "3. Carpet Cleaning\n"
        response += "4. Window Cleaning"

    # PLUMBING SERVICES
    elif text == '1*2':
        response = "CON Plumbing Services\n"
        response += "1. Pipe Repair\n"
        response += "2. Toilet Repair\n"
        response += "3. Water Tank Installation\n"
        response += "4. Drainage Unblocking"

    # ELECTRICAL SERVICES
    elif text == '1*3':
        response = "CON Electrical Services\n"
        response += "1. House Wiring\n"
        response += "2. Socket Repair\n"
        response += "3. Lighting Installation\n"
        response += "4. Solar Installation"

    # BUILDING SERVICES
    elif text == '1*4':
        response = "CON Building & Repairs\n"
        response += "1. Brick Laying\n"
        response += "2. House Renovation\n"
        response += "3. Roofing Repair\n"
        response += "4. Painting"

    # HOME CARE
    elif text == '1*5':
        response = "CON Home Care Services\n"
        response += "1. House Maid\n"
        response += "2. Babysitting\n"
        response += "3. Elderly Care\n"
        response += "4. Cooking Services"

    # MY APPOINTMENTS
    elif text == '2':
        response = "END You have no appointments yet."

    # CUSTOMER SUPPORT
    elif text == '3':
        response = "END Contact HomiCare Support on +256700000000"

    # INVALID
    else:
        response = "END Invalid choice"

    return HttpResponse(response, content_type="text/plain")