from .models import SupportTicket, TicketMessage


def create_ticket(user, category, subject, description):

    ticket = SupportTicket.objects.create(
        user=user,
        category=category,
        subject=subject,
        description=description
    )

    return ticket


def reply_ticket(ticket, sender, message):

    reply = TicketMessage.objects.create(
        ticket=ticket,
        sender=sender,
        message=message
    )

    ticket.status = "in_progress"
    ticket.save()

    return reply


def close_ticket(ticket):

    ticket.status = "closed"
    ticket.save()

    return ticket