from rest_framework import serializers

from .models import Review, ReviewReply, ReviewHelpful


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"


class ReviewReplySerializer(serializers.ModelSerializer):

    class Meta:
        model = ReviewReply
        fields = "__all__"


class ReviewHelpfulSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReviewHelpful
        fields = "__all__"