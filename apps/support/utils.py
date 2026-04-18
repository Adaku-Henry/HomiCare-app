def ticket_is_open(ticket):

    return ticket.status in ["open", "in_progress"]


def ticket_is_closed(ticket):

    return ticket.status == "closed"