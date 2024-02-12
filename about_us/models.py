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

