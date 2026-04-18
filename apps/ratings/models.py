from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Review(models.Model):

    RATING_CHOICES = (
        (1, "1 Star"),
        (2, "2 Stars"),
        (3, "3 Stars"),
        (4, "4 Stars"),
        (5, "5 Stars"),
    )

    VISIBILITY_CHOICES = (
        ("visible", "Visible"),
        ("hidden", "Hidden"),
    )

    booking = models.OneToOneField(
        "bookings.Booking",
        on_delete=models.CASCADE,
        related_name="booking_review"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_reviews"
    )

    provider = models.ForeignKey(
        "providers.ProviderProfile",
        on_delete=models.CASCADE,
        related_name="ratings_reviews"
    )

    rating = models.IntegerField(choices=RATING_CHOICES)

    comment = models.TextField(blank=True)

    visibility = models.CharField(
        max_length=10,
        choices=VISIBILITY_CHOICES,
        default="visible"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.rating} stars"


class ReviewReply(models.Model):

    review = models.OneToOneField(
        Review,
        on_delete=models.CASCADE,
        related_name="provider_reply"
    )

    provider = models.ForeignKey(
        "providers.ProviderProfile",
        on_delete=models.CASCADE,
        related_name="review_replies"
    )

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reply by {self.provider}"


class ReviewHelpful(models.Model):

    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name="helpful_votes"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="helpful_reviews"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} found review helpful"