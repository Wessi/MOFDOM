from modeltranslation.translator import translator, TranslationOptions
from .models import About


class AboutTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(About, AboutTranslationOptions)
