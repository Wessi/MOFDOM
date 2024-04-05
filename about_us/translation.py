from modeltranslation.translator import register,TranslationOptions
from .models import About, TeamMember, BureauStructure, Service

@register(About)
class AboutTranslationOption(TranslationOptions):
    fields = ('title',"content")

@register(TeamMember)
class TeamMemberTranslationOption(TranslationOptions):
    fields = ('name', 'role' )

@register(BureauStructure)
class StructureTranslationOption(TranslationOptions):
    fields = ('title', 'content', 'management_board_title')


@register(Service)
class ServiceTranslationOption(TranslationOptions):
    fields = ('title', 'content')
