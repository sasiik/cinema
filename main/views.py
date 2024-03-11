from django.shortcuts import render
from event.views import parse_events
from news.views import parse_news
from event.models import Types

# Show data on main page

def display_home(request):
    event_types = (type.title for type in Types.objects.all())
    arguments = {}
    for type in event_types:
        arguments[f'{type}s_items'] = parse_events(request, type)
    arguments['news_items'] = parse_news()
    return render(request, 'home.html', arguments)

