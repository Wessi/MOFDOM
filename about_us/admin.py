from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


admin.site.register(TeamMember)
# admin.site.register(About)
admin.site.register(BureauStructure)


@admin.register(About)
class AboutAdmin(TranslationAdmin):
    list_display = ("title",)
    

