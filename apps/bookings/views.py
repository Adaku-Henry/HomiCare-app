from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Booking, BookingRating
from .serializers import BookingSerializer, BookingRatingSerializer
from .services import accept_booking, start_job, complete_job, cancel_booking
from apps.wallet.models import WalletTransaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    @action(detail=True, methods=['post'])
    def accept(self, request, pk=None):
        booking = self.get_object()
        accept_booking(booking)
        return Response({"status": "Bookings accepted"})

    @action(detail=True, methods=['post'])
    def start(self, request, pk=None):
        booking = self.get_object()
        start_job(booking)
        return Response({"status": "Job started"})

    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        booking = self.get_object()
        complete_job(booking)
        # Trigger wallet payment
        WalletTransaction.objects.create(
            wallet=booking.user.wallet,
            amount=booking.total_price,
            transaction_type='SPEND',
            reference=booking.reference,
            description=f"Payment for booking {booking.reference}"
        )
        return Response({"status": "Job completed and payment triggered"})

    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        booking = self.get_object()
        cancel_booking(booking)
        return Response({"status": "Bookings cancelled"})

    @action(detail=True, methods=['post'])
    def rate(self, request, pk=None):
        booking = self.get_object()
        data = request.data
        rating, created = BookingRating.objects.update_or_create(
            booking=booking,
            defaults={'rating': data.get('rating', 5), 'review': data.get('review', '')}
        )
        return Response({"status": "Rating saved"})



class BookingListCreateView(APIView):
    def get(self, request):
        return Response({"message": "GET bookings works"})

    def post(self, request):
        return Response({"message": "POST booking works"}, status=status.HTTP_201_CREATED)


class BookingDetailView(APIView):
    def get(self, request, pk):
        return Response({"message": f"Booking {pk}"})