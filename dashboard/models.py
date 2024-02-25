from django.db import models
from django.contrib.auth.models import User
# Create your model
from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from django.utils.translation import gettext as _ 


class GalleryImage(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery_images/')

    CATEGORY_CHOICES = [
        ('LEADERSHIP', 'LEADERSHIP'),
        ('MEETINGS', 'MEETINGS'),
        ('EVENTS/SEMINARS', 'EVENTS/SEMINARS'),
        ('EMPLOYEES', 'EMPLOYEES'),
        ('OFFICE', 'OFFICE'),
        ('channal one', 'channal one'),
    ]

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title

class Slider(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    content = models.TextField()
    button_text = models.CharField(max_length=50)
    image = models.ImageField(upload_to='slider_images/')
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
        
class About_us_index(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    button_text = models.CharField(max_length=250)
    image = models.ImageField(upload_to='slider_images/')
    def __str__(self):
        return self.title
            
class FeaturedWork(models.Model):
    title = models.CharField(max_length=255)
    background_image = models.ImageField(upload_to='featured_work_backgrounds/')
    description = models.TextField()

    def __str__(self):
        return self.title

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    def __str__(self):
        return self.question

class Footer(models.Model):
    about_us_content = models.TextField()
    contact_info = models.TextField()
    projects_links = models.TextField()
    quick_links = models.TextField()
    newsletter_content = models.TextField()
    copyright_text = models.CharField(max_length=255)
    
    
#2/13/2024
class ContactInfo(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    working_hours = models.CharField(max_length=100)  # Adding working hours

class QuickLink(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()

class Newsletter(models.Model):
    description = models.TextField()  # Adding description field

#2/13/2024


class Event(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='event_images')
    time = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()

class TestBlog(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_("Title"), max_length=200),
        desc = models.CharField(_("Description"), max_length=200),
        name = models.CharField(_("Name"), max_length=200),
        
        
    )

    def __unicode__(self):
        return self.title