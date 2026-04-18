from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    SupportTicketViewSet,
    TicketMessageViewSet,
    TicketCategoryViewSet
)

router = DefaultRouter()

router.register("tickets", SupportTicketViewSet)

router.register("messages", TicketMessageViewSet)

router.register("categories", TicketCategoryViewSet)

urlpatterns = [

    path("", include(router.urls)),

]