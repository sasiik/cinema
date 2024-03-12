from django.db import models
from datetime import date
from django.db.models import CheckConstraint, Q, UniqueConstraint
from django.db.models.functions import Now

# Model for event types
class Types(models.Model):
    title = models.CharField(max_length=32)
    
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name_plural = "Types"
        
    # Custom save method to ensure title is lowercase
    def save(self, *args, **kwargs):
        self.title = self.title.lower()  # Convert name to lowercase
        super().save(*args, **kwargs) 

# Model for event locations
class EventLocation(models.Model):
    event_type = models.ForeignKey(Types, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    places_count = models.IntegerField()

    class Meta:
        constraints = [
            # Constraint to ensure places_count is non-negative
            CheckConstraint(check=Q(places_count__gt=0), name='event_places_count_positive')
        ]
        
    def __str__(self):
        return f"{self.name}"

# Main event model
class Event(models.Model):
    title = models.CharField(max_length=100)
    short_desc = models.TextField(max_length=256)
    desc = models.TextField()
    location = models.ForeignKey(EventLocation, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/events/') # I should handle images differently
    date = models.DateField(default=date(1970, 1, 1))
    is_available = models.BooleanField(default=True)
    available_places = models.IntegerField()

    class Meta:
        constraints = [
            # Constraint to ensure event date is in the future
            CheckConstraint(check=Q(date__gte=Now()), name='event_date_future'),
            # Constraint to ensure available places couut >= 0
            CheckConstraint(check=Q(available_places__gte=0), name='positive_available_places'),
            # Constraint to ensure unique title-date combination
            UniqueConstraint(fields=['title', 'date'], name='unique_event_title_date')
        ]
        
    def __str__(self):
        return f"{self.title}"
    
    # def save(self, *args, **kwargs):
    #     if self.available_places is None:
    #         self.available_places = self.location.places_count
    #         super(Event, self).save(*args, **kwargs)