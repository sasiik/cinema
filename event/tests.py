from datetime import date
from .models import Event, Types, EventLocation  # Replace 'yourapp' with the actual name of your Django app

# Ensure there are Types for "film" and "event"
film_type, _ = Types.objects.get_or_create(title="film")
event_type, _ = Types.objects.get_or_create(title="event")

locations_data = [
            {"event_type": event_type, "name": "Location 1 for Events", "places_count": 15},
            {"event_type": event_type, "name": "Location 2 for Events", "places_count": 30},
            {"event_type": film_type, "name": "Location 1 for Films", "places_count": 15},
            {"event_type": film_type, "name": "Location 2 for Films", "places_count": 30}
            ]

locations = []
for location in locations_data:
    created_location, _ = EventLocation.objects.get_or_create(event_type=location["event_type"], name=location["name"], places_count=location["places_count"])
    locations.append(created_location)


# List of event details, alternating types
event_details = [
    {"title": "Event 1", "date": date(2024, 4, 10), "is_available": True, "location": locations[0]},
    {"title": "Event 2", "date": date(2024, 3, 15), "is_available": False, "location": locations[1]},
    {"title": "Event 3", "date": date(2024, 3, 20), "is_available": True, "location": locations[0]},
    {"title": "Event 4", "date": date(2024, 4, 25), "is_available": True, "location": locations[0]},
    {"title": "Event 5", "date": date(2024, 5, 30), "is_available": False, "location": locations[2]},
    {"title": "Event 6", "date": date(2024, 6, 5), "is_available": True, "location": locations[3]},
    {"title": "Event 7", "date": date(2024, 7, 10), "is_available": True, "location": locations[2]},
    {"title": "Event 8", "date": date(2024, 8, 15), "is_available": False, "location": locations[3]},
]

# Create or update events, alternating types
for detail in event_details:
    event, created = Event.objects.update_or_create(
        title=detail["title"],
        defaults={
            "short_desc": "Short description for " + detail["title"],
            "desc": "Long description for " + detail["title"],
            "location": detail["location"],
            "image": "path/to/image.jpg",  # Replace with a valid image path
            "date": detail["date"],
            "is_available": detail["is_available"],
        }
    )
    print(f'{"Created" if created else "Updated"} {event.title} as a {"film" if detail["location"].event_type == film_type else "event"}')
