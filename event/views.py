from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from user.models import CustomUser, Ticket
from .models import Event
from .forms import ParticipateForm



def get_available_places(event): 
    places_taken = Ticket.objects.filter(event=event).count()
    available_places = event.location.places_count - places_taken
    return available_places
    
def parse_events(request):
    events = Event.objects.filter(location__event_type__title="event")
    return events

def parse_films(request):
    films = Event.objects.filter(location__event_type__title="film")
    return films

def event_page(request, event_id):
    current_event = Event.objects.get(id=event_id)
    if current_event.location.event_type.title == 'event':
        return render(request, 'event.html', {"image": current_event.image, "location": current_event.location, "title": current_event.title, "desc": current_event.desc, "event_id": current_event.id, "is_available": current_event.is_available, "date": current_event.date, "places_available": get_available_places(current_event)})
    return render(request, 'film.html', {"image": current_event.image, "location": current_event.location, "title": current_event.title, "desc": current_event.desc, "event_id": current_event.id, "is_available": current_event.is_available, "date": current_event.date, "places_available": get_available_places(current_event)})

@login_required
def participate(request):
    if request.method == 'POST':
        form = ParticipateForm(request.POST)
        if form.is_valid():
            event_id = form.cleaned_data['event_id']
            event = get_object_or_404(Event, pk=event_id)
            if not Ticket.objects.filter(user=request.user, event=event):
                available_places = get_available_places(event)
                if available_places > 0:
                    current_participants_count = Ticket.objects.filter(event=event).count()
                    user_event = Ticket.objects.create(user=request.user, event=event, place=current_participants_count+1)
                    event.save()
                    if available_places - 1 == 0:
                        event.is_available = 0
                        event.save()
                    messages.success(request, 'You have successfully participated!')
                else:
                    messages.error(request, 'Sorry, no more places available.')
            else:
                messages.error(request, 'You are already participating in this event.')

            return redirect('event_page', event_id=event_id)
    return redirect('home')