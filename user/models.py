from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date
from django.db.models import UniqueConstraint, CheckConstraint, Q
from event.models import Event



# Custom User table
class CustomUser(AbstractUser):
    
    def __str__(self):
        return self.username

# Table for Users' tickets to the Events 

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_tickets')
    place = models.IntegerField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_tickets')

    class Meta:
       constraints = [
            # Unique constraint and Check constraint that ensures that place number >= 0
            UniqueConstraint(fields=['user', 'event'], name='unique_user_event', violation_error_message="Pair user-event already exists"),
            CheckConstraint(check=Q(place__gte=0), name='ticket_place_positive')
        ]

    def __str__(self):
        return f"{self.user.username} joined {self.event.title}, Place {self.place}"