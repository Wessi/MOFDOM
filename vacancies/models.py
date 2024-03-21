from django.db import models

class Job(models.Model):
    job_description = models.TextField(null=True, blank=True)
    job_title = models.CharField(max_length=255,help_text="Make sure to submit a max of 255 characters.")
    job_type = models.CharField(max_length=50, choices=[
        ('Contract', 'Contract'),
        ('Freelance', 'Freelance'),
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Internship', 'Internship'),
    ])
    Status = models.CharField(max_length=50, choices=[
        ('Active', 'Active'),
        ('CLosed', 'Closed'),
    ])
    vacancies = models.IntegerField(choices=[
        (1, 1),
        (2, 2),
        (5, 5),
        (10, 10),
    ])
    skills = models.CharField(max_length=255,help_text="Make sure to submit a max of 255 characters.")
    job_deadline = models.DateField()
    location = models.CharField(max_length=255, default='',help_text="Make sure to submit a max of 255 characters.")  # Assuming location is a character field

    level = models.CharField(max_length=255, choices=[
        ('Junior', 'Junior'),
        ('Mid-Level', 'Mid-Level'),  # Removed extra space
        ('Senior', 'Senior'),  # Corrected capitalization
        ('Expert', 'Expert'),
    ])

    class Meta:
        ordering = ("-id",)
    def __str__(self):
        return self.job_title

    def get_list_fields():
        return ['job_title', 'job_type', 'Status', 'job_deadline']
    
    list_fields = get_list_fields()


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete = models.CASCADE,)
    name = models.CharField(max_length = 255, )
    email = models.EmailField()
    cv = models.FileField(blank=False)
    created_date = models.DateTimeField(auto_now_add =True)

    def __str__(self) -> str:
        return f"Application from '{self.name}' for : {self.job}"

