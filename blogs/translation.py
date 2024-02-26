from .models import Blog
from modeltranslation.translator import TranslationOptions, register

@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ("title", "content")

