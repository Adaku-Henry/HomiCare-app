from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Review, ReviewReply, ReviewHelpful
from .serializers import (
    ReviewSerializer,
    ReviewReplySerializer,
    ReviewHelpfulSerializer
)


class ReviewViewSet(viewsets.ModelViewSet):

    queryset = Review.objects.all()

    serializer_class = ReviewSerializer

    permission_classes = [IsAuthenticated]


class ReviewReplyViewSet(viewsets.ModelViewSet):

    queryset = ReviewReply.objects.all()

    serializer_class = ReviewReplySerializer

    permission_classes = [IsAuthenticated]


class ReviewHelpfulViewSet(viewsets.ModelViewSet):

    queryset = ReviewHelpful.objects.all()

    serializer_class = ReviewHelpfulSerializer

    permission_classes = [IsAuthenticated]