from django.contrib.auth.models import AbstractUser
from django.db import models
from event.models import Event

class CustomUser(AbstractUser):
    user_events = models.ManyToManyField(Event, through='UserEvent')

    def __str__(self):
        return self.username