# models.py

from django.db import models

class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    content = models.TextField()
    button_text = models.CharField(max_length=50)

class AboutUsTP(models.Model):
    title = models.CharField(max_length=200)
    paragraph1 = models.TextField()
    paragraph2 = models.TextField()
    image = models.ImageField(upload_to='about_images/')

    def __str__(self):
        return self.title

class MissionVisionValues(models.Model):
    mission_title = models.CharField(max_length=100)
    mission_description = models.TextField()
    vision_title = models.CharField(max_length=100)
    vision_description = models.TextField()
    values_title = models.CharField(max_length=100)
    values_description = models.TextField()

    def __str__(self):
        return f"{self.mission_title} - {self.vision_title} - {self.values_title}"

class FinishProject(models.Model):
    project_count = models.IntegerField(default=0)
    offices_count = models.IntegerField(default=0)
    employees_count = models.IntegerField(default=0)
    awards_count = models.IntegerField(default=0)

    def __str__(self):
        return f"Projects: {self.project_count}, Offices: {self.offices_count}, Employees: {self.employees_count}, Awards: {self.awards_count}"

class Partner(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField()
    logo = models.ImageField(upload_to='partner_logos/')

    def __str__(self):
        return self.name
        
        
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