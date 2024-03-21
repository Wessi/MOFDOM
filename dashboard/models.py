from django.db import models
from django.db import models
from django.utils.translation import gettext as _ 

CATEGORY_CHOICES = (
        ('LEADERSHIP', 'LEADERSHIP'),
        ('MEETINGS', 'MEETINGS'),
        ('EVENTS/SEMINARS', 'EVENTS/SEMINARS'),
        ('EMPLOYEES', 'EMPLOYEES'),
        ('OFFICE', 'OFFICE'),
        ('channal one', 'channal one'),
)

class GalleryCategory(models.Model):
    # List of categories for Gallery pages
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    def get_list_fields():
        return ['name']
    
    list_fields = get_list_fields()

class GalleryImage(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery_images/', help_text="Please select an image with close width and height resolution (400p x 300px).")
    gallery_category = models.ForeignKey(GalleryCategory, on_delete = models.SET_NULL, null=True) 
    
    class Meta:
        ordering = ("-id",)

    def __str__(self):
        return self.title
    
    def category(self):
        return self.gallery_category if self.gallery_category else ""
    
    def get_list_fields():
        return ['title', 'gallery_category']
    
    list_fields = get_list_fields()

class GalleryVideo(models.Model):
    title = models.CharField(max_length =255)
    video = models.FileField(upload_to="Gallery/Videos", blank=True, null=True)
    link = models.CharField(max_length=10000, blank=True,default="")
    gallery_category = models.ForeignKey(GalleryCategory, on_delete = models.SET_NULL, null=True) 
    
    class Meta:
        ordering = ("-id",)

    def __str__(self):
        return self.title
    
    def category(self):
        return self.gallery_category if self.gallery_category else ""
    
    def get_list_fields():
        return ['title', 'gallery_category']
    
    list_fields = get_list_fields()

class DirectorateMessage(models.Model):
    # A message from the bureau director displayed at the homepage
    is_single = True # Tells if the model should have multiple or single objects

    title = models.CharField(max_length=255)
    content = models.TextField()
    button_text = models.CharField(max_length=250)
    image = models.ImageField(upload_to='slider_images/')
    
    def __str__(self):
        return self.title



class FeaturedWork(models.Model):
    # Slider contents displayed at the home page
    title = models.CharField(max_length=255)
    background_image = models.ImageField(upload_to='featured_work_backgrounds/')
    description = models.TextField()

    class Meta:
        ordering = ("-id",)
        verbose_name = _("Home Page Sliders")
        verbose_name_plural = _("Home Page Sliders")
    
    def __str__(self):
        return self.title
    
    def get_list_fields():
        return ['title', 'description']
    
    list_fields = get_list_fields()
    
    
class FAQ(models.Model):
    # List of Frequently Asked Questions with their corresponding answers
    question = models.CharField(max_length=255)
    answer = models.TextField()
    
    def __str__(self):
        return self.question
    
    class Meta:
        ordering = ("-id",)
    
    def get_list_fields():
        return ['question', 'answer']
    
    list_fields = get_list_fields()
    
    
class QuickLink(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()

    def get_list_fields():
        return ['title', 'url']
    
    list_fields = get_list_fields()


class Event(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='event_images')
    time = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()

    def get_list_fields():
        return ['title', 'time', 'location', 'date']
    
    list_fields = get_list_fields()