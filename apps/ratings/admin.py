from django.contrib import admin
from .models import Review, ReviewReply, ReviewHelpful


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "provider",
        "rating",
        "visibility",
        "created_at",
    )

    list_filter = (
        "rating",
        "visibility",
        "created_at",
    )

    search_fields = (
        "user__username",
        "comment",
    )


@admin.register(ReviewReply)
class ReviewReplyAdmin(admin.ModelAdmin):

    list_display = (
        "provider",
        "review",
        "created_at",
    )


@admin.register(ReviewHelpful)
class ReviewHelpfulAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "review",
        "created_at",
    )