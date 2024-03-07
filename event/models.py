from django.db import models
from datetime import date
from django.db.models import CheckConstraint, Q, UniqueConstraint
from django.db.models.functions import Now

class Types(models.Model):
    title = models.CharField(max_length=32)
    
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name_plural = "Types"
        
    def save(self, *args, **kwargs):
        self.title = self.title.lower()  # Convert name to lowercase
        super().save(*args, **kwargs) 

class EventLocation(models.Model):
    event_type = models.ForeignKey(Types, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    places_count = models.IntegerField()

    class Meta:
        constraints = [
            CheckConstraint(check=Q(places_count__gte=0), name='event_places_count_positive')
        ]
    def __str__(self):
        return f"{self.name}"

    
# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    short_desc = models.TextField(max_length=256)
    desc = models.TextField()
    location = models.ForeignKey(EventLocation, on_delete=models.CASCADE)
    image = models.ImageField()
    date = models.DateField(default=date(1970, 1, 1))
    is_available = models.BooleanField(default=True)

    class Meta:
        constraints = [
            CheckConstraint(check=Q(date__gte=Now()), name='event_date_future'),
            UniqueConstraint(fields=['title', 'date'], name='unique_event_title_date')
        ]
    
    def __str__(self):
        return f"{self.title}"




