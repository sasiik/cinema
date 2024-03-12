from event.models import Event
from user.models import Ticket


class BaseParser:
    def __init__(self, request):
        self.request = request

    def get_events(self):
        raise NotImplementedError("Subclasses must implement this method.")

class EventParser(BaseParser):
    def get_events(self):
        return Event.objects.filter(location__event_type__title="event")

class FilmParser(BaseParser):
    def get_events(self):
        return Event.objects.filter(location__event_type__title="film")
    
class MyTicketsParser(BaseParser):
    def get_events(self):
        return Ticket.objects.filter(user_id=self.request.user.id)


class ParserFactory:
    @staticmethod
    def get_parser(event_type, request):
        parsers = {
            'event': EventParser,
            'film': FilmParser,
            'my_tickets': MyTicketsParser,
            # Add more mappings as needed
        }
        parser = parsers.get(event_type)
        if parser:
            return parser(request)
        raise ValueError("Invalid event type")