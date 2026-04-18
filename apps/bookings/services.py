def accept_booking(booking):
    booking.status = "ACCEPTED"
    booking.save()

def start_job(booking):
    booking.status = "IN_PROGRESS"
    booking.save()

def complete_job(booking):
    booking.status = "COMPLETED"
    booking.save()

def cancel_booking(booking):
    booking.status = "CANCELLED"
    booking.save()