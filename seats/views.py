from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from event.models import Event
from user.models import UserEvent
from .hall_config import create_iteration
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from event.forms import ParticipateForm


@login_required
def choice(request, event_id):
    if request.method == 'POST':
        form = ParticipateForm(request.POST)
        if form.is_valid():
            event_id = form.cleaned_data['event_id']
            event = get_object_or_404(Event, pk=event_id)
            if not event in request.user.user_events.all():
                if event.places_count > 0:
                    place = form.cleaned_data['selected_seat']
                    if place:
                        seat_taken = UserEvent.objects.filter(event=event, place=place).exists()
                        if not seat_taken:
                            user_event = UserEvent.objects.create(user=request.user, event=event, place=place)
                            event.places_count -= 1
                            event.save()
                            if event.places_count == 0:
                                event.is_available = False
                                event.save()
                            messages.success(request, 'You have successfully participated!')
                        else:
                            messages.error(request, 'This seat is already taken.')
                    else:
                        messages.error(request, 'Select a place.')
                else:
                    messages.error(request, 'Sorry, no more places available.')
            else:
                messages.error(request, 'You are already participating in this event.')
            return redirect('event_page', event_id=event_id)

    elif request.method == 'GET':
        event = Event.objects.get(pk=event_id)
        taken_places = [str(elem.place) for elem in UserEvent.objects.filter(event=event)]
        if event.event_type.title == 'film':
            if event.places_count > 0:
                return render(request, 'choose_seat.html', {"iteration": create_iteration(6, 9), "event_id": event_id, "taken_places": taken_places})
            return redirect('event_page', event_id=event_id)
    return redirect('home')