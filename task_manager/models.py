from django.db import models
from accounts.models import UserProfile
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
# Task Status Choices
STATUS_CHOICES = (
    ('New', 'New'),
    ('Completed', 'Completed'),
    ('Inprogress', 'Inprogress'),
    ('Pending', 'Pending'),
)

# Priority Choices
PRIORITY_CHOICES = (
    ('High', 'High'),
    ('Medium', 'Medium'),
    ('Low', 'Low'),
)

class Task(models.Model):
    assigned_to = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='assigned_tasks')
    task_name = models.CharField(max_length=255)

    assigned_date = models.DateTimeField()
    due_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='Medium')
    task_description = models.TextField()
    key_tasks = models.TextField()

    def __str__(self):
        return self.task_name
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
@receiver(post_save, sender=Comment)
def create_comment_notification(sender, instance, created, **kwargs):
    if created:
        # Create a notification when a new comment is added
        Notification.objects.create(
            user=instance.task.assigned_to,
            message=f"New comment added to task: {instance.task.task_name}"
        )

@receiver(post_save, sender=Task)
def create_task_notification(sender, instance, created, **kwargs):
    if created:
        # Create a notification when a new task is created
        Notification.objects.create(
            user=instance.assigned_to,
            message=f"New task created: {instance.task_name}"
        )