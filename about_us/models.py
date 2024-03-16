# models.py

from django.db import models

class About(models.Model):
    # Model for the detail page of about us page
    title = models.CharField(max_length=100)
    content = models.TextField()
    mission = models.TextField()
    vision = models.TextField()
    values = models.TextField()
    image_one = models.ImageField(upload_to='about_images/', blank=False)
    image_two = models.ImageField(upload_to='about_images/', blank=False)
    image_three = models.ImageField(upload_to='about_images/', blank=False)

    def __str__(self):
        return f"About Page Content {self.id}"

class TeamMember(models.Model):
    # Model for the section inside the about us, which lists Management experts
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team_members/')
    social_facebook = models.URLField(blank=True)
    social_twitter = models.URLField(blank=True)
    social_google_plus = models.URLField(blank=True)

    def __str__(self):
        return f"{self.name} | {self.role}"


class BureauStructure(models.Model):
    # Model for the Bureau structure page
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='bureau_structure_images/')
    management_board_title = models.CharField(max_length=100)
    management_board_content = models.TextField()
    execution_team_title = models.CharField(max_length=100)
    execution_team_content = models.TextField()
    execution_team_image = models.ImageField(upload_to='bureau_structure_images/')

    def __str__(self):
        return f"Bureau Structure Content {self.id}"