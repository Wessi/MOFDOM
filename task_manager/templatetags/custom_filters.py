# task_manager/templatetags/custom_tags.py
from django import template
from task_manager.models import Task  # Correct import statement
import os
register = template.Library()
from django.conf import settings
from pathlib import Path


@register.simple_tag
def get_task_count_by_status(status):
    return Task.objects.filter(status=status).count()


@register.filter(name='get_key_tasks')
def get_key_tasks(task):
    return task.key_tasks.split('\n') if task.key_tasks else []

@register.filter(name='show_attrs')
def show_attrs(obj):
    # print("*"*20,"\n", dir(obj),"*"*20,"\n")
    return None

@register.filter()
def get_file_name(pdf_url):
    file_name = os.path.basename(pdf_url) 
    f = Path(os.path.join(settings.MEDIA_ROOT,"documents/", file_name))
    if f.is_file() :
        return file_name
    return False
    
