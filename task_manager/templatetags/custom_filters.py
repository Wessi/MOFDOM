# task_manager/templatetags/custom_tags.py
from django import template
from task_manager.models import Task  # Correct import statement

register = template.Library()

@register.simple_tag
def get_task_count_by_status(status):
    return Task.objects.filter(status=status).count()
@register.filter(name='get_key_tasks')
def get_key_tasks(task):
    return task.key_tasks.split('\n') if task.key_tasks else []