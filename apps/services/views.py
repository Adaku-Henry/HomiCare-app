from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import ServiceCategory, Service
from .serializers import ServiceCategorySerializer, ServiceSerializer


class ServiceCategoryViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = ServiceCategory.objects.filter(is_active=True)
    serializer_class = ServiceCategorySerializer
    lookup_field = "slug"


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Service.objects.filter(is_available=True)
    serializer_class = ServiceSerializer

    filter_backends = [SearchFilter, OrderingFilter]

    search_fields = ["name", "description"]

    ordering_fields = ["base_price", "popularity_score"]