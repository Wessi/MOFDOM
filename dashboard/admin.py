from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(FeaturedWork)
admin.site.register(GalleryImage)
admin.site.register(Slider)
admin.site.register(FAQ)
# admin.site.register(ContactInfo)
admin.site.register(QuickLink)
admin.site.register(Newsletter)
admin.site.register(Event)
admin.site.register(About_us_index)
admin.site.register(TestBlog)

from django.middleware.locale import LocaleMiddleware

