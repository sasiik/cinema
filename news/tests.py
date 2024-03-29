from .models import News 

# Example details for News objects
news_details = [
    {"title": "News 1", "short_desc": "Short description for News 1", "full_link": "http://example.com/news1", "image_path": "images/news/test_image.jpg"},
    {"title": "News 2", "short_desc": "Short description for News 2", "full_link": "http://example.com/news2", "image_path": "images/news/test_image.jpg"},
    {"title": "News 3", "short_desc": "Short description for News 3", "full_link": "http://example.com/news3", "image_path": "images/news/test_image.jpg"},
    {"title": "News 4", "short_desc": "Short description for News 4", "full_link": "http://example.com/news4", "image_path": "images/news/test_image.jpg"},
    {"title": "News 5", "short_desc": "Short description for News 5", "full_link": "http://example.com/news5", "image_path": "images/news/test_image.jpg"},
    {"title": "News 6", "short_desc": "Short description for News 6", "full_link": "http://example.com/news6", "image_path": "images/news/test_image.jpg"},
]

for detail in news_details:
    news, created = News.objects.get_or_create(
        title=detail["title"],
        defaults={
            "short_desc": detail["short_desc"],
            "full_link": detail["full_link"],
            "image": detail['image_path'],
        }
    )
    print(f'{"Created" if created else "Updated"} {news.title}')

