from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from user.models import CustomUser, Ticket
from .models import Event
from .forms import ParticipateForm


def parse_events(request):
    events = Event.objects.filter(event_type__title="event")
    return events

def parse_films(request):
    films = Event.objects.filter(event_type__title="film")
    return films

def event_page(request, event_id):
    current_event = Event.objects.get(id=event_id)
    if current_event.event_type.title == 'event':
        return render(request, 'event.html', {"image": current_event.image, "places_count": current_event.places_count, "title": current_event.title, "desc": current_event.desc, "event_id": current_event.id, "date": current_event.date})
    return render(request, 'film.html', {"image": current_event.image, "places_count": current_event.places_count, "title": current_event.title, "desc": current_event.desc, "event_id": current_event.id, "date": current_event.date})

@login_required
def participate(request):
    if request.method == 'POST':
        form = ParticipateForm(request.POST)
        if form.is_valid():
            event_id = form.cleaned_data['event_id']
            event = get_object_or_404(Event, pk=event_id)
            if not event in request.user.user_events.all():
                if event.places_count > 0:
                    current_participants_count = len(CustomUser.objects.filter(user_event_links__event=event))
                    user_event = Ticket.objects.create(user=request.user, event=event, place=current_participants_count+1)
                    event.places_count -= 1
                    event.save()
                    if event.places_count == 0:
                        event.is_available = 0
                        event.save()
                    messages.success(request, 'You have successfully participated!')
                else:
                    messages.error(request, 'Sorry, no more places available.')
            else:
                messages.error(request, 'You are already participating in this event.')

            return redirect('event_page', event_id=event_id, messages=messages)
    return redirect('home')