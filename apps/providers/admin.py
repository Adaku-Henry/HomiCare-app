from django.contrib import admin
from .models import (
    ProviderProfile,
    ProviderService,
    ProviderPortfolio,
    ProviderAvailability,
    ProviderVerification,
    ProviderReview,
    ProviderNotification
)

admin.site.register(ProviderProfile)
admin.site.register(ProviderService)
admin.site.register(ProviderPortfolio)
admin.site.register(ProviderAvailability)
admin.site.register(ProviderVerification)
admin.site.register(ProviderReview)
admin.site.register(ProviderNotification)