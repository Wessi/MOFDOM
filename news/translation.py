from .models import NewsArticle
from modeltranslation.translator import TranslationOptions, register

@register(NewsArticle)
class BlogTranslationOptions(TranslationOptions):
    fields = ("title", )

