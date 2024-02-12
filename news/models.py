from django.db import models

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


class Cat(models.Model):
    name = models.CharField(max_length=50)
    count = models.IntegerField(default=0)  # To count how many news contains in an one category

    def __str__(self):
        return self.name


class Comment(models.Model):

    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    cm = models.TextField()
    news_id = models.IntegerField()
    date = models.CharField(max_length=15)
    time = models.CharField(max_length=15)
    status = models.IntegerField(default=0) # to give permission a comment

    def __str__(self):
        return self.name


class Trending(models.Model):
    txt = models.CharField(max_length=200)

    def __str__(self):
        return self.txt


class Main(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    abouttxt = models.TextField(default="")
    fb = models.CharField(default="-", max_length=50)
    tw = models.CharField(default="-", max_length=50)
    yt = models.CharField(default="-", max_length=50)
    tell = models.CharField(default="-", max_length=50)
    link = models.CharField(default="-", max_length=50)

    set_name = models.CharField(default="-", max_length=50)

    ## for header and footer logo images start
    picurl = models.TextField(default="")
    picname = models.TextField(default="")

    picurl2 = models.TextField(default="")
    picname2 = models.TextField(default="")

    ## for header and footer logo images end

    def __str__(self):
        return self.set_name + " | " + str(self.pk)


class SubCat(models.Model):
    name = models.CharField(max_length=50)
    catname = models.CharField(max_length=50)  # main category name
    catid = models.IntegerField()
    def __str__(self):
        return self.name


class Newsletter(models.Model):
    txt = models.CharField(max_length=70)  ## email or phone number
    status = models.IntegerField()

    def __str__(self):
        return self.txt
    