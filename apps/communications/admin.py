from django.contrib import admin
from .models import Conversation, Message, CallLog, Notification

admin.site.register(Conversation)
admin.site.register(Message)
admin.site.register(CallLog)
admin.site.register(Notification)