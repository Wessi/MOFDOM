from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

@admin.register(About)
class AboutAdmin(TranslationAdmin):
    list_display = ("title","content")

@admin.register(BureauStructure)
class BureauStructureAdmin(TranslationAdmin):
    group_fieldsets = True
    list_display = ("title","content")

admin.site.register(TeamMember)

