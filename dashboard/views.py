from django.views import View
from django.db.models.base import ModelBase
from django.shortcuts import render,redirect
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin
from core.forms import get_form
from .forms import *
from .models import *
from about_us.models import About, TeamMember, BureauStructure
from about_us.forms import AboutForm, TeamMemberForm, BureauStructureForm
from dashboard.models import FeaturedWork, GalleryCategory, GalleryImage, GalleryVideo, DirectorateMessage, FAQ, QuickLink, Event

model_conf = {  #key     : [model]
                'sliders': [FeaturedWork, ],
                'about'  : [About,  ], 
                'team'   : [TeamMember,  ] ,
                'bureau' : [BureauStructure,  ],

            }

class Dashboard(LoginRequiredMixin, View ):
    def get(self, request):
        return render(request, 'admin_home.html')
    

def get_conf(request, kwargs):
    if 'model_name' in kwargs and kwargs['model_name'] in model_conf.keys():
        conf = model_conf[kwargs['model_name']]
        model:ModelBase = conf[0]
        model_name:str = model._meta.verbose_name or kwargs['model_name'].capitalize()
        form =  get_form(model)
        has_many = getattr(model,'is_single',False)
        return {"model":conf[0], "form":form, "model_name": model_name,"single": not has_many}
    
    else:
        # messages.error(request, "Page not found!")
        return redirect("admin_dashboard")



class CreateView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        config = get_conf(self.request, self.kwargs)
        model, model_name  = config["model"], config["model_name"] 
        form = config["form"] 
        if config["single"] and model.objects.first(): # if model object has to be generated only once
            return redirect("change_view", model_name = kwargs['model_name'], pk=model.objects.first().id)
        
        return render(self.request, 'staff/create_page.html', { 'add':True,  'form':form, 'is_single':config["single"], 
                                                                'model_name':model_name.capitalize(),})
    
    def post(self, *args, **kwargs):
        config = get_conf(self.request, self.kwargs)
        model = config["model"]
        form = config["form"]
        if form.is_valid():
            obj  = form.save(commit = False)
            if hasattr(model, 'created_by'):
                setattr(obj, 'created_by', self.request.user)
            obj.save()
            return redirect("admin_dashboard" )
        model_name = config["model_name"]
        return render(self.request, 'staff/create_page.html', { 'add':True,  'form':form, 'is_single':config["single"], 
                                                                'model_name':model_name.capitalize(),})
        


class ChangeView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        config = get_conf(self.request,self.kwargs)
        model, model_name = config["model"], config["model_name"]
        
        # if model is single, just bring the first object
        if config['single']:
            obj = model.objects.first()
            # if there is no object created for this single item page, redirect to create view
            if not obj: 
                return redirect("create_view", model_name = model_name)
        
        # If model can have multiple objects, fetch the object with the pk
        else: 
            obj = model.objects.get(id = self.kwargs['pk'])
        form = config["form"](instance = obj)
        return render(self.request, 'staff/create_page.html', { 'add':False,  'form':form, 'is_single':config['single'], 
                                                                'model_name':model_name.capitalize(),})
    
    def post(self, *args, **kwargs):
        config = get_conf(self.request,self.kwargs)
        model, model_name = config["model"], config["model_name"]
        obj = model.objects.get(id = self.kwargs['pk'])
        form = config["form"](self.request.POST,self.request.FILES,instance = obj)
        if form.is_valid():
            form.save()
            return redirect("admin_dashboard")
        
        print(form.errors)
        return render(self.request, 'staff/create_page.html', { 'add':False,  'form':form, 'is_single':config['single'], 
                                                                'model_name':model_name.capitalize(),})
    
        



class ListView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        if 'model_name' in kwargs and kwargs['model_name'] in model_conf.keys():
            conf = model_conf[self.kwargs['model_name']]
            if conf[2]:
                return redirect("change_view", model_name=self.kwargs['model_name'])
            
            model:ModelBase = conf[0]
            model_name:str = model._meta.verbose_name or self.kwargs['model_name'].capitalize()
            
            if conf[2] and model.objects.first(): # if model object has to be generated only once
                return redirect("change_view", model_name = self.kwargs['model_name'])
            


