from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Conversation(models.Model):
    """Represents a chat session between two or more users."""
    participants = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.id} with {self.participants.count()} participants"


class Message(models.Model):
    """General message model for chat, SMS, USSD, etc."""
    MESSAGE_TYPE_CHOICES = (
        ('text', 'Text'),
        ('image', 'Image'),
        ('audio', 'Audio'),
        ('video', 'Video'),
        ('sms', 'SMS'),
        ('ussd', 'USSD'),
        ('system', 'System'),
        ('voice_call', 'Voice Call'),
        ('video_call', 'Video Call'),
    )

    STATUS_CHOICES = (
        ('sent', 'Sent'),
        ('delivered', 'Delivered'),
        ('read', 'Read'),
        ('failed', 'Failed'),
    )

    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField(blank=True, null=True)
    attachment = models.FileField(upload_to='message_attachments/', blank=True, null=True)
    message_type = models.CharField(max_length=20, choices=MESSAGE_TYPE_CHOICES, default='text')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='sent')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} to {self.recipient} ({self.message_type})"


class CallLog(models.Model):
    CALL_TYPE_CHOICES = (
        ('voice', 'Voice'),
        ('video', 'Video'),
    )

    STATUS_CHOICES = (
        ('missed', 'Missed'),
        ('completed', 'Completed'),
        ('rejected', 'Rejected'),
        ('ongoing', 'Ongoing'),
    )

    caller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='outgoing_calls')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incoming_calls')
    call_type = models.CharField(max_length=10, choices=CALL_TYPE_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)

    def __str__(self):
        return f"{self.call_type.capitalize()} Call from {self.caller} to {self.receiver}"


class Notification(models.Model):
    NOTIF_TYPE_CHOICES = (
        ('booking_update', 'Bookings Update'),
        ('message', 'Message'),
        ('system', 'System Alert'),
        ('reminder', 'Reminder'),
        ('promo', 'Promotional'),
    )

    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=255)
    message = models.TextField()
    type = models.CharField(max_length=30, choices=NOTIF_TYPE_CHOICES)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} - {self.title}"