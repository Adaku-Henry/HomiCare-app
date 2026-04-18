from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import UserActivity, ServiceAnalytics, RevenueAnalytics
from .serializers import UserActivitySerializer, ServiceAnalyticsSerializer, RevenueAnalyticsSerializer


class UserActivityView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        activity = UserActivity.objects.get(user=request.user)
        serializer = UserActivitySerializer(activity)
        return Response(serializer.data)


class ServiceAnalyticsView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        analytics = ServiceAnalytics.objects.all()
        serializer = ServiceAnalyticsSerializer(analytics, many=True)
        return Response(serializer.data)


class RevenueAnalyticsView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        revenue = RevenueAnalytics.objects.all().order_by('-date')[:30]
        serializer = RevenueAnalyticsSerializer(revenue, many=True)
        return Response(serializer.data)


from django.shortcuts import render

# Create your views here.
