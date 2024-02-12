from .models import NewsArticle
from django.contrib import admin
from .models import *
admin.site.register(NewsArticle)
admin.site.register(News)
admin.site.register(Trending)
admin.site.register(Comment)
admin.site.register(Cat)
admin.site.register(SubCat)
