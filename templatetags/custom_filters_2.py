# yourapp/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter(name='split_links')
def split_links(value, delimiter=','):
    return value.split(delimiter)
