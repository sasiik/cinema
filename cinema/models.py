from django.contrib.auth.models import AbstractUser
from event.models import Event
from django.db import models

class CustomUser(AbstractUser):
    my_events = models.ManyToManyField(Event)

    def __str__(self):
        return self.username
