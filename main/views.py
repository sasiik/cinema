from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from news.views import parse_news
from event.views import parse_events, parse_films
from news.views import parse_news

def show_data(request):
    news_items = parse_news(request)
    events_items = parse_events(request)
    films_items = parse_films(request)
    return render(request, 'home.html', {'news_items': news_items, 'events_items': events_items, 'films_items': films_items})

def redirect_to_home(request):
    return redirect('home')
