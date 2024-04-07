from modeltranslation.translator import register,TranslationOptions
from .models import About, TeamMember, BureauStructure, Service

@register(About)
class AboutTranslationOption(TranslationOptions):
    fields = ('title',"content", "mission", "vision", "values")

@register(TeamMember)
class TeamMemberTranslationOption(TranslationOptions):
    fields = ('name', 'role' )

@register(BureauStructure)
class StructureTranslationOption(TranslationOptions):
    fields = ('title', 'content', 'management_board_title', 'management_board_content', 'execution_team_title', 'execution_team_content')


@register(Service)
class ServiceTranslationOption(TranslationOptions):
    fields = ('title', 'content')
