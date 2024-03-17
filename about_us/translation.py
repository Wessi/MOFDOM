from modeltranslation.translator import translator, register,TranslationOptions
from .models import About, BureauStructure

@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title',"content")

@register(BureauStructure)
class StructureTO(TranslationOptions):
    fields = ('title', 'content', 'management_board_title')
