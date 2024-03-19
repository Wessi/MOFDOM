from modeltranslation.translator import translator, register,TranslationOptions
from .models import About, TeamMember, BureauStructure

@register(About)
class AboutTranslationOption(TranslationOptions):
    fields = ('title',"content")

@register(TeamMember)
class TeamMemberTranslationOption(TranslationOptions):
    fields = ('name', 'role' )

@register(BureauStructure)
class StructureTranslationOption(TranslationOptions):
    fields = ('title', 'content', 'management_board_title')

