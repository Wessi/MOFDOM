# views.py

from django.shortcuts import render
from .models import *
from dashboard.models import ContactInfo, QuickLink
#def about_us(request):
    #about_us_data = AboutUs.objects.first()  # Assuming there is only one About Us entry
    #return render(request, 'about_us/about_us.html', {'about_us_data': about_us_data})
def about_us(request):
    return render(request, 'about_us.html')

def contact_us(request):
    return render(request, 'contact_us.html')
def directories(request):
    return render(request, 'our_directories.html')
def directories_detail(request):
    return render(request, 'directorie_detail.html')
def our_structure(request):
    return render(request, 'our_structure.html')
    
#2/13/2023    
def about(request):
    about_data = About.objects.first()
    team_members = TeamMember.objects.all()

    context = {
        'about_data': about_data,
        'team_members': team_members,
    }

    return render(request, 'front/about.html', context)
# views.py

def bureau_structure(request):
    structure_data = BureauStructure.objects.first()
    # Fetch Footer data
    contact_info = ContactInfo.objects.first()
    quick_links = QuickLink.objects.all()
    
    
    return render(request, 'front/structure.html', {'structure_data': structure_data, 'contact_info': contact_info, 'quick_links': quick_links, })
