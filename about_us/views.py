from django.shortcuts import render, redirect
from django.views import View
from .models import *
from .forms import AboutForm
from django.db.models.base import ModelBase

 
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


class CreateAbout(View):
    def get(self, request):
        return render(request, 'create_about.html',{'form':AboutForm()})
    def post(self, request):
        form = AboutForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("admin_dashboard")
        return render(request, 'create_about.html',{'form':form})

