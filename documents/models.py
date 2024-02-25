from django.db import models
import os

def get_file_extension(filename):
    return os.path.splitext(filename)[1]
class Document(models.Model):
    CATEGORY_CHOICES = (
        ('BPR Documentations', 'BPR Documentations'),
        ('Regulations', 'Regulations'),
        ('Declarations', 'Declarations'),
        ('Annual Report', 'Annual Report'),
        ('Other', 'Other'),
    )
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES, default='OTH')
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.title
    def file_extension(self):
        return get_file_extension(self.file.name)
    