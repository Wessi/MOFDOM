from .models import NewsArticle
from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

@admin.register(NewsArticle)
class NewsArticleAdmin(TranslationAdmin):
    list_display = ("title","content")


admin.site.register(NewsCategory)
# admin.site.register(News)
# admin.site.register(Trending)
