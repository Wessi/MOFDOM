from modeltranslation.translator import translator, TranslationOptions
from .models import AboutUs , About


class AboutTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(About, AboutTranslationOptions)
