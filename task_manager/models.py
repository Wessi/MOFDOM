from django.db import models
from accounts.models import UserProfile
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext as _
# Task Status Choices
STATUS_CHOICES = (
    ('New', _('New')),
    ('Completed', _('Completed')),
    ('Inprogress', _('Inprogress')),
    ('Pending', _('Pending')),
)

# Priority Choices
PRIORITY_CHOICES = (
    ('High', _('High')),
    ('Medium', _('Medium')),
    ('Low', _('Low')),
)

class Task(models.Model):
    assigned_to = models.ManyToManyField(UserProfile, related_name='assigned_tasks')
    monitoring = models.ManyToManyField(UserProfile, related_name='monitoring_tasks')
    task_name = models.CharField(max_length=255)

    assigned_date = models.DateTimeField(auto_now_add=True, editable = True)
    start_date = models.DateTimeField( blank=True, null=True)
    due_date = models.DateTimeField( blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='Medium')
    task_description = models.TextField()
    key_tasks = models.TextField()

    def __str__(self):
        return self.task_name
    
    def get_list_fields():
        return ['task_name', 'description']
    
    list_fields = get_list_fields()
    
class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    def __str__(self):
        return f"Comment by {self.user.username} on {self.task.task_name}"


class Notification(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
# @receiver(post_save, sender=Comment)
# def create_comment_notification(sender, instance, created, **kwargs):
#     if created:
#         Notification.objects.create(
#             user=instance.task.assigned_to,
#             message=f"New comment added to task: {instance.task.task_name}"
#         )

# @receiver(post_save, sender=Task)
# def create_task_notification(sender, instance, created, **kwargs):
#     if created:
#         Notification.objects.create(
#             user=instance.assigned_to,
#             message=f"New task created: {instance.task_name}"
#         )