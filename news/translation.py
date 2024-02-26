from .models import NewsArticle, News
from modeltranslation.translator import TranslationOptions, register

@register(NewsArticle)
class BlogTranslationOptions(TranslationOptions):
    fields = ("title", )

