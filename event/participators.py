from django.shortcuts import get_object_or_404, redirect
from event.forms import ParticipateForm
from django.contrib import messages

from user.models import Ticket

from event.models import Event


class BaseParticipate:
    def __init__(self, request, event_id):
        self.request = request
        self.event_id = event_id
        self.event = get_object_or_404(Event, pk=event_id)

    def participate(self):
        raise NotImplementedError("Subclasses must implement this method.")

class ParticipateEvent(BaseParticipate):
    def participate(self):
        # Logic for participating in a general event
        if self.request.method == 'POST':
            form = ParticipateForm(self.request.POST)
            if form.is_valid():
                event_id = form.cleaned_data['event_id']
                event = get_object_or_404(Event, pk=event_id)
                # Check if user is already participating in the event
                if not Ticket.objects.filter(user=self.request.user, event=event):
                    available_places = event.available_places
                    # Check if there are available places for the user to participate
                    if available_places > 0:
                        current_participants_count = Ticket.objects.filter(event=event).count()
                        # Create a new ticket for the user to participate in the event
                        Ticket.objects.create(user=self.request.user, event=event, place=current_participants_count+1)
                        messages.success(self.request, 'You have successfully participated!')
                    else:
                        messages.error(self.request, 'Sorry, no more places available.')
                else:
                    messages.error(self.request, 'You are already participating in this event.')

                return redirect('event_page', event_id=event_id)
        return redirect('home')

class ParticipateFilm(BaseParticipate):
    def participate(self):
        # Logic for participating in a film event
        if self.request.method == 'POST':
            form = ParticipateForm(self.request.POST)
            if form.is_valid():
                event_id = form.cleaned_data['event_id']
                event = get_object_or_404(Event, pk=event_id)
                # Check if user is already participating in the event
                if not Ticket.objects.filter(user=self.request.user, event=event):
                    # Check if there are available places for the user to participate
                    available_places = event.available_places
                    if available_places > 0:
                        place = form.cleaned_data['selected_seat']
                        # Check if the seat exists and is not taken
                        if place:
                            seat_taken = Ticket.objects.filter(event=event, place=place).exists()
                            if not seat_taken:
                                Ticket.objects.create(user=self.request.user, event=event, place=place)
                                messages.success(self.request, 'You have successfully participated!')
                            else:
                                messages.error(self.request, 'This seat is already taken.')
                        else:
                            messages.error(self.request, 'Select a place.')
                    else:
                        messages.error(self.request, 'Sorry, no more places available.')
                else:
                    messages.error(self.request, 'You are already participating in this event.')
                return redirect('event_page', event_id=event_id)
        return redirect('home')

class ParticipateFactory:
    @staticmethod
    def get_participation(event_type, request, event_id):
        participations = {
            'event': ParticipateEvent,
            'film': ParticipateFilm,
            # Add more mappings as needed
        }
        participate_class = participations.get(event_type)
        if participate_class:
            return participate_class(request, event_id)
        raise ValueError("Invalid event type")
