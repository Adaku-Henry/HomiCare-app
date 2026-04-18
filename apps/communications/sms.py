from .africastalking_client import sms


def send_sms(recipient_number, message):

    try:
        response = sms.send(message, [recipient_number])
        return response

    except Exception as e:
        print("SMS Error:", e)
        return None