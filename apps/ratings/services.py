from .models import Review, ReviewHelpful
from apps.providers.models import Provider


def create_review(user, booking, rating, comment):

    provider = booking.provider

    review = Review.objects.create(
        user=user,
        booking=booking,
        provider=provider,
        rating=rating,
        comment=comment
    )

    update_provider_rating(provider)

    return review


def update_provider_rating(provider):

    reviews = Review.objects.filter(provider=provider)

    total = sum(r.rating for r in reviews)

    count = reviews.count()

    if count == 0:
        avg = 0
    else:
        avg = total / count

    provider.average_rating = avg
    provider.save()


def mark_review_helpful(user, review):

    return ReviewHelpful.objects.create(
        user=user,
        review=review
    )