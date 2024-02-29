from django.db import models
from datetime import date

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    short_desc = models.TextField(max_length=256)
    desc = models.TextField()
    location = models.ForeignKey(EventLocation, on_delete=models.CASCADE)
    image = models.ImageField()
    date = models.DateField(default=date(1970, 1, 1))
    is_available = models.BooleanField()

    

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    place = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        unique_together = ('user', 'event')  # Optional: ensures uniqueness

    def __str__(self):
        return f"{self.user.username} joined {self.event.title} on {self.date_joined}"

class EventLocation(models.Model):
    event_type = models.ForeignKey(Types, on_delete=models.CASCADE)
    name = models.TextField()
    places_count = models.IntegerField()


