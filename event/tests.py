from datetime import date
from .models import Event, Types  # Replace 'yourapp' with the actual name of your Django app

# Ensure there are Types for "film" and "event"
film_type, _ = Types.objects.get_or_create(title="film")
event_type, _ = Types.objects.get_or_create(title="event")

# List of event details, alternating types
event_details = [
    {"title": "Event 1", "type": film_type, "date": date(2024, 1, 10), "places_count": 25, "is_available": True},
    {"title": "Event 2", "type": event_type, "date": date(2024, 2, 15), "places_count": 0, "is_available": False},
    {"title": "Event 3", "type": film_type, "date": date(2024, 3, 20), "places_count": 50, "is_available": True},
    {"title": "Event 4", "type": event_type, "date": date(2024, 4, 25), "places_count": 100, "is_available": True},
    {"title": "Event 5", "type": film_type, "date": date(2024, 5, 30), "places_count": 0, "is_available": False},
    {"title": "Event 6", "type": event_type, "date": date(2024, 6, 5), "places_count": 20, "is_available": True},
    {"title": "Event 7", "type": film_type, "date": date(2024, 7, 10), "places_count": 95, "is_available": True},
    {"title": "Event 8", "type": event_type, "date": date(2024, 8, 15), "places_count": 0, "is_available": False},
]

# Create or update events, alternating types
for detail in event_details:
    event, created = Event.objects.update_or_create(
        title=detail["title"],
        defaults={
            "event_type": detail["type"],
            "short_desc": "Short description for " + detail["title"],
            "desc": "Long description for " + detail["title"],
            "image": "path/to/image.jpg",  # Replace with a valid image path
            "date": detail["date"],
            "places_count": detail["places_count"],
            "is_available": detail["is_available"],
        }
    )
    print(f'{"Created" if created else "Updated"} {event.title} as a {"film" if detail["type"] == film_type else "event"}')
