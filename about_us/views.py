# views.py

from django.shortcuts import render
from django.views import View
from .models import *

 
def about(request): # Render about us page 
    about_data = About.objects.first()
    team_members = TeamMember.objects.all()
    context = {
        'about_data': about_data,
        'team_members': team_members,
    }

    return render(request, 'front/about.html', context)


def bureau_structure(request):
    structure_data = BureauStructure.objects.first()
    
    return render(request, 'front/structure.html', {'structure_data': structure_data})
