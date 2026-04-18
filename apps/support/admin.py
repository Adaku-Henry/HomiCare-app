from django.contrib import admin

from .models import SupportTicket, TicketMessage, TicketCategory


admin.site.register(SupportTicket)

admin.site.register(TicketMessage)

admin.site.register(TicketCategory)