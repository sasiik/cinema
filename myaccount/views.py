from django.http import JsonResponse
from django.shortcuts import redirect, render
from cinema.parsers import ParserFactory
from django.views.decorators.http import require_POST
from event.models import Event
from django.contrib import messages

from user.models import Ticket

# Create your views here.

def display_myaccount(request):
    my_tickets_queryset = ParserFactory.get_parser('my_tickets', request).get_events()
    my_tickets = list(my_tickets_queryset.values('place', 'event_id'))

    # Fetch all relevant Event objects in a single query
    event_ids = [ticket['event_id'] for ticket in my_tickets]
    events = Event.objects.filter(id__in=event_ids).values('id', 'title')

    # Create a mapping of event IDs to event titles
    event_id_to_name = {event['id']: event['title'] for event in events}

    # Replace event_id in my_tickets with event title using the mapping
    for ticket in my_tickets:
        event_id = ticket["event_id"]  # Remove event_id
        ticket['event_name'] = event_id_to_name.get(event_id, 'Unknown Event')  # Add event_name

    arguments = {
        'user': request.user,
        'my_tickets': my_tickets
    }

    return render(request, 'myaccount.html', arguments)

@require_POST  # Ensure this view only accepts POST requests to improve security
def delete_item(request):
    event_id = request.POST.get('selected_event')
    if event_id:
        try:
            item = Ticket.objects.get(event_id=event_id)
            item.delete()
        except Event.DoesNotExist:
            messages.error(request, "Event does not exist")
    return redirect('myaccount')