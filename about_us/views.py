# views.py

from django.shortcuts import render
from django.views import View

from .models import *
from dashboard.models import ContactInfo, QuickLink

 
def about(request):
    # Render about us page 
    about_data = About.objects.first()
    team_members = TeamMember.objects.all()
    context = {
        'about_data': about_data,
        'team_members': team_members,
    }

    return render(request, 'front/about.html', context)


def bureau_structure(request):
    structure_data = BureauStructure.objects.first()
    
    # Fetch Footer data
    contact_info = ContactInfo.objects.first()
    quick_links = QuickLink.objects.all()
    
    
    return render(request, 'front/structure.html', {'structure_data': structure_data, 'contact_info': contact_info, 'quick_links': quick_links, })
