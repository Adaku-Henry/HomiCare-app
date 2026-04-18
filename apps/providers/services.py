from .models import ProviderProfile


def update_provider_rating(provider):

    reviews = provider.reviews.all()

    if not reviews.exists():
        return

    total = sum(review.rating for review in reviews)

    provider.rating = total / reviews.count()

    provider.total_reviews = reviews.count()

    provider.save()