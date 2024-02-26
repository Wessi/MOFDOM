# models.py

from django.db import models

class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    content = models.TextField()
    button_text = models.CharField(max_length=50)

        
#2/13/2024       
class About(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    mission = models.TextField()
    vision = models.TextField()
    values = models.TextField()
    image_one = models.ImageField(upload_to='about_images/', blank=False)
    image_two = models.ImageField(upload_to='about_images/', blank=False)
    image_three = models.ImageField(upload_to='about_images/', blank=False)

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team_members/')
    social_facebook = models.URLField(blank=True)
    social_twitter = models.URLField(blank=True)
    social_google_plus = models.URLField(blank=True)

class BureauStructure(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='bureau_structure_images/')
    management_board_title = models.CharField(max_length=100)
    management_board_content = models.TextField()
    execution_team_title = models.CharField(max_length=100)
    execution_team_content = models.TextField()
    execution_team_image = models.ImageField(upload_to='bureau_structure_images/')