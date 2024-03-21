from django.db import models

class About(models.Model):
    """ Model for the detail page of about us page"""
    is_single = True # Tells if the model should have multiple or single objects
    title = models.CharField(max_length=100, help_text= "Max of 100 Characters.")
    content = models.TextField(help_text= "Make sure that the has a max of 500 words.")
    mission = models.TextField(help_text= "Make sure that the has a max of 500 words.")
    vision = models.TextField(help_text= "Make sure that the has a max of 500 words.")
    values = models.TextField(help_text= "Make sure that the has a max of 500 words.")
    image_one = models.ImageField(upload_to='about_images/', blank=False, help_text="Make sure to submit 200 X 300 images.")
    image_two = models.ImageField(upload_to='about_images/', blank=False, help_text="Make sure to submit 200 X 300 images.")
    image_three = models.ImageField(upload_to='about_images/', blank=False, help_text="Make sure to submit 200 X 300 images.")
    
    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"
    
    
    def __str__(self):
        return f"About Page Content"
    

class TeamMember(models.Model):
    # Model for the section inside the about us, which lists Management experts
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team_members/', help_text="Make sure to submit 300 X 400 images.")
    social_facebook = models.URLField(blank=True)
    social_twitter = models.URLField(blank=True)
    social_google_plus = models.URLField(blank=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return f"{self.name} | {self.role}"

    def get_list_fields():
        return ['name', 'role',]
    list_fields = get_list_fields()
    
    
class BureauStructure(models.Model):
    is_single = True # Tells if the model should have multiple or single objects
    # Model for the Bureau structure page
    title = models.CharField(max_length=100, help_text="Make sure to submit a max of 50 words.")
    content = models.TextField(help_text="Make sure to submit a content that aligns with the height of the image")
    image = models.ImageField(upload_to='bureau_structure_images/', help_text="Make sure to submit an image proportional to the content")
    management_board_title = models.CharField(max_length=100,help_text="Make sure to submit a max of 100 characters.")
    management_board_content = models.TextField(help_text="Make sure to submit a content that aligns with the height of the image")
    execution_team_title = models.CharField(max_length=100,help_text="Make sure to submit a max of 100 characters.")
    execution_team_content = models.TextField(help_text="Make sure to submit a content that aligns with the height of the image")
    execution_team_image = models.ImageField(upload_to='bureau_structure_images/',
                                             help_text="Make sure to submit an image proportional to the execution team content")

    def __str__(self):
        return f"Bureau Structure Content "