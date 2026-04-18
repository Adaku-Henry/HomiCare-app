# africastalking_client.py
import africastalking
from django.conf import settings

def get_at_instance():
    africastalking.initialize(
        settings.AFRICASTALKING_USERNAME,
        settings.AFRICASTALKING_API_KEY
    )
    return africastalking

def ussd_callback(request):
    at = get_at_instance()
    # use `at` to send USSD/SMS etc.