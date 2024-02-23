from django.db import models


class Types(models.Model):
    title = models.CharField(max_length=32)
# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    event_type = models.ForeignKey(Types, on_delete=models.CASCADE)
    short_desc = models.TextField(max_length=256)
    desc = models.TextField()
    image = models.ImageField()
    places_count = models.IntegerField()
    is_available = models.BooleanField()