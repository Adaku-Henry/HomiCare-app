from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .services import process_booking_payment, subscribe_user, refund_payment
from .models import Payment, SubscriptionPlan, UserSubscription
from .serializers import PaymentSerializer, SubscriptionPlanSerializer, UserSubscriptionSerializer

# --- Bookings Payment ---
class BookingPaymentView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        booking = request.data.get('booking')
        amount = request.data.get('amount')
        payment = process_booking_payment(request.user, booking, amount)
        serializer = PaymentSerializer(payment)
        return Response(serializer.data)

# --- Subscribe to Plan ---
class SubscribeView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        plan_id = request.data.get('plan_id')
        subscription, payment = subscribe_user(request.user, plan_id)
        serializer = UserSubscriptionSerializer(subscription)
        return Response(serializer.data)

# --- Refund Payment ---
class RefundPaymentView(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request):
        payment_id = request.data.get('payment_id')
        payment = refund_payment(payment_id)
        serializer = PaymentSerializer(payment)
        return Response(serializer.data)

# --- List Plans ---
class SubscriptionPlanListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        plans = SubscriptionPlan.objects.all()
        serializer = SubscriptionPlanSerializer(plans, many=True)
        return Response(serializer.data)