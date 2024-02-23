from django.shortcuts import render
from .models import News
# Create your views here.

def parse_news(request):
    news = News.objects.all()
    return news
