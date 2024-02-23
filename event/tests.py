from django.test import TestCase
from .models import Event
# Create your tests here.
event = Event.objects.create(
    title='Test Event',
    event_type_id=1,  # replace with an actual id from your Types model
    short_desc='A short description',
    desc='A detailed description',
    image='path/to/image.png',  # replace with a valid path or use an ImageField-compatible method
    places_count=100,
    is_available='True'  # This should raise an error
)

# If no error is raised, check what is stored
print(event.is_available)