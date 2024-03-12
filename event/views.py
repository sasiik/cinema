from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from cinema.parsers import ParserFactory

from event.participators import ParticipateFactory
from .models import Event

# Function to parse events


def parse_events(request, event_type):
    parsed_data = ParserFactory.get_parser(event_type, request).get_events()
    return parsed_data

# Fuction to display events


def display_event(request, event_id):

    supported_pages = {
        'film': 'film.html',
        'event': 'event.html'
    }
    current_event = Event.objects.get(id=event_id)
    event_type = current_event.location.event_type.title
    template_name = supported_pages[event_type]

    arguments = {
        "image": current_event.image,
        "location": current_event.location,
        "title": current_event.title,
        "desc": current_event.desc,
        "event_id": event_id,
        "is_available": current_event.is_available,
        "date": current_event.date,
        "places_available": current_event.available_places,
        # "is_participating": current_event.event_tickets.objects.filter(user=request.user) consider in future to make cancel buttons
    }
    return render(request, template_name, arguments)

# Function to participate in the event using forms


@login_required
def participate(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    event_type = event.location.event_type.title.lower()
    participant = ParticipateFactory.get_participation(
        event_type, request, event_id)
    return participant.participate()
