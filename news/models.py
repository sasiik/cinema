from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=32)
    short_desc = models.TextField(max_length=256)
    full_link = models.TextField()
    image = models.ImageField(upload_to='images/news/')
    
    class Meta:
        verbose_name_plural = "News"
        
    def __str__(self):
        return f"{self.title}"