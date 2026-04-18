def generate_booking_reference(booking_id, user_id, date):
    return f"HC-{user_id}-{date.strftime('%Y%m%d')}-{booking_id}"