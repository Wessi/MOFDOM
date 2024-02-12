# documents/templatetags/document_categories_tags.py

from django import template
from .models import Document

register = template.Library()

@register.inclusion_tag('partials/document_categories.html')
def render_document_categories():
    document_categories = {}
    for category, _ in Document.CATEGORY_CHOICES:
        documents = Document.objects.filter(category=category)
        document_categories[category] = documents

    return {'document_categories': document_categories}
