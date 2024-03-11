from django.shortcuts import render
from .models import News

# News parser
def parse_news():
    news = News.objects.all()
    return news
