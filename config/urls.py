from django.contrib import admin
from django.urls import path, include
from apps.bookings.views import BookingListCreateView, BookingDetailView

urlpatterns = [

    path('admin/', admin.site.urls),

    path('api/users/', include('apps.users.urls')),
    path('api/communication/', include('apps.communications.urls')),
    path('api/wallet/', include('apps.wallet.urls')),
    path("api/services/", include("apps.services.urls")),
    path("api/providers/", include("apps.providers.urls")),
    path('api/analytics/', include('apps.analytics.urls')),
    path("api/subscriptions/", include("apps.subscriptions.urls")),
    path("api/support/", include("apps.support.urls")),
    path("api/ratings/", include("apps.ratings.urls")),

    # ✅ BOOKINGS (FIXED)
    path('api/bookings/', BookingListCreateView.as_view()),
    path('api/bookings/<int:pk>/', BookingDetailView.as_view()),
]