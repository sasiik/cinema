from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from event.models import Event
from user.models import Ticket
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from event.forms import ParticipateForm


def divide_seats_into_rows(seats_per_row, seats_count):
    if seats_per_row > 0 and seats_count > 0:
        rows_count = seats_count // seats_per_row
        last_row = seats_count % seats_per_row
        result = [[i+j*seats_per_row for i in range(1, seats_per_row+1)] for j in range(rows_count)] + [[i+rows_count*seats_per_row for i in range(1, last_row+1)]]
        return result
    else:
        return ValueError("Seats per row or seats count are not positive numbers")
        
# Function to display seats 
        
def display_seats(request, event_id):
    event = Event.objects.get(pk=event_id)
    taken_places = [elem.place for elem in Ticket.objects.filter(event=event)]
    arguments = {
        "iteration": divide_seats_into_rows(10, event.location.places_count),
        "event_id": event_id, 
        "taken_places": taken_places
        }
    if event.location.places_count > 0:
        return render(request, 'choose_seat.html', arguments)
    return redirect('event_page', event_id=event_id)