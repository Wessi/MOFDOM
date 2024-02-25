from django.db import models

class ContactUs(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    subject = models.CharField(max_length=300)
    message = models.TextField()
    sent_date =models.DateField( auto_now_add = True )

    def __str__(self):
        return f"Message from : {self.full_name}"
    
    class Meta:
        ordering = ('-id',)


class Settings(models.Model):
    title = models.CharField(max_length=255, blank=False, default ="Bureau of Finance")
    logo = models.ImageField(upload_to="Logo")
    phone1 = models.CharField(max_length=255, blank=False, )
    phone2 = models.CharField(max_length=255, blank=True,default = "" )
    email = models.EmailField(blank=True)
    email_for_contact_us = models.EmailField(blank=True)
    facebook = models.CharField(max_length=255, blank=True, default ="")
    youtube = models.CharField(max_length=255, blank=True, default ="")
    instagram = models.CharField(max_length=255, blank=True, default ="")
    twitter = models.CharField(max_length=255, blank=True, default ="")
    linkedin = models.CharField(max_length=255, blank=True, default ="")
    address = models.CharField(max_length=255, blank=False, default ="")
    working_hours = models.CharField(max_length=100)  # Adding working hours
    map_link = models.TextField( blank=True, null=True, help_text = "Embed the full 'iframe' tag from google maps" )



class Pages(models.Model):
    about = models.BooleanField(default = True)
    structure = models.BooleanField(default = True)
    directorate = models.BooleanField(default = True)
    documents = models.BooleanField(default = True)
    gallery = models.BooleanField(default = True)
    vacancy = models.BooleanField(default = True)
    events = models.BooleanField(default = True)
    news = models.BooleanField(default = True)
    resource = models.BooleanField(default = True)
    contact_us = models.BooleanField(default = True)
    privacy = models.BooleanField(default = True)
    

    def __str__(self):
        return f"Page Controller {self.id}"

    class Meta:
        ordering =('-id',)
