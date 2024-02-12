# views.py

from django.shortcuts import render
from .models import AboutUs

#def about_us(request):
    #about_us_data = AboutUs.objects.first()  # Assuming there is only one About Us entry
    #return render(request, 'about_us/about_us.html', {'about_us_data': about_us_data})
def about_us(request):
    return render(request, 'about_us.html')
def about_us_edit(request):
    return render(request, 'about.html')
def contact_us(request):
    return render(request, 'contact_us.html')
def directories(request):
    return render(request, 'our_directories.html')
def directories_detail(request):
    return render(request, 'directorie_detail.html')
def our_structure(request):
    return render(request, 'our_structure.html')
