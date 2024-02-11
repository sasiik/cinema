from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def home(request):
    news_items = [{'title': f'News {i}', 'text': f'Content of news {i}.'} for i in range(1, 7)]
    return render(request, 'home.html', {'news_items': news_items})
