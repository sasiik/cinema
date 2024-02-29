from django.core.files import File  # Import if you're setting images from local paths
from .models import News  # Replace 'yourapp' with your actual app name

# Example details for News objects
news_details = [
    {"title": "News 1", "short_desc": "Short description for News 1", "full_link": "http://example.com/news1", "image_path": "/path/to/image1.jpg"},
    {"title": "News 2", "short_desc": "Short description for News 2", "full_link": "http://example.com/news2", "image_path": "/path/to/image2.jpg"},
    {"title": "News 3", "short_desc": "Short description for News 3", "full_link": "http://example.com/news3", "image_path": "/path/to/image3.jpg"},
    {"title": "News 4", "short_desc": "Short description for News 4", "full_link": "http://example.com/news4", "image_path": "/path/to/image4.jpg"},
    {"title": "News 5", "short_desc": "Short description for News 5", "full_link": "http://example.com/news5", "image_path": "/path/to/image5.jpg"},
    {"title": "News 6", "short_desc": "Short description for News 6", "full_link": "http://example.com/news6", "image_path": "/path/to/image6.jpg"},
]

for detail in news_details:
    news, created = News.objects.get_or_create(
        title=detail["title"],
        defaults={
            "short_desc": detail["short_desc"],
            "full_link": detail["full_link"],
            # Assuming you're handling images as File objects, or adjust as necessary for your setup
            "image": detail['image_path'],
        }
    )
    print(f'{"Created" if created else "Updated"} {news.title}')
from django.test import TestCase

# Create your tests here.
