from django.db import models
from django.contrib.postgres.indexes import GinIndex

# Create your models here.
#from wagtail.models import Page
#class NewsPage(Page):
    #pass


class NewsArticle(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    content = models.TextField()
    featured_image = models.ImageField(upload_to='news_images/')
    minutes_read = models.IntegerField()
    likes = models.IntegerField(default=0)
    category = models.CharField(max_length=100)  # Add a category field
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('-id',)

        
    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    content = models.TextField()
    featured_image = models.ImageField(upload_to='news_images/')
    minutes_read = models.IntegerField()
    likes = models.IntegerField(default=0)
    category = models.CharField(max_length=100)  # Add a category field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


