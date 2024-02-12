from django.db import models

class Job(models.Model):
    job_description = models.TextField(null=True, blank=True)
    job_title = models.CharField(max_length=255)
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
    skills = models.CharField(max_length=255)
    job_deadline = models.DateField()
    locationn = models.CharField(max_length=255, default='')  # Assuming location is a character field

    level = models.CharField(max_length=255, choices=[
        ('Junior', 'Junior'),
        ('Mid-Level', 'Mid-Level'),  # Removed extra space
        ('Senior', 'Senior'),  # Corrected capitalization
        ('Expert', 'Expert'),
    ])

    def __str__(self):
        return self.job_title
