from django.contrib import admin
from .models import Booking, BookingAttachment, BookingRating

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("reference", "user", "provider", "total_price", "status", "booking_date", "booking_time")
    list_filter = ("status", "emergency", "recurring")
    search_fields = ("user__username", "provider__user__username", "reference")

@admin.register(BookingAttachment)
class BookingAttachmentAdmin(admin.ModelAdmin):
    list_display = ("booking", "image", "description")

@admin.register(BookingRating)
class BookingRatingAdmin(admin.ModelAdmin):
    list_display = ("booking", "rating", "review")