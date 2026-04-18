from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    ReviewViewSet,
    ReviewReplyViewSet,
    ReviewHelpfulViewSet
)

router = DefaultRouter()

router.register("reviews", ReviewViewSet)

router.register("replies", ReviewReplyViewSet)

router.register("helpful", ReviewHelpfulViewSet)

urlpatterns = [

    path("", include(router.urls)),

]