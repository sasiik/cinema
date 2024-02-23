from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=32)
    short_desc = models.TextField(max_length=256)
    full_link = models.TextField()
    image = models.ImageField()