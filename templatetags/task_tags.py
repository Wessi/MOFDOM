from django import template
from task_manager.models import Task

register = template.Library()

@register.simple_tag
def get_task_count_by_status(status):
    return Task.objects.filter(status=status).count()
