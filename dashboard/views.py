from django.views import View
from django.apps import apps
from django.conf import settings
from django.db.models.base import ModelBase
from django.shortcuts import render,redirect
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from core.forms import get_form
from task_manager.models import Task 
from vacancies.models import Job, Application
from dashboard.models import Event 

def get_model(name):
    # app_labels = ['about_us','blogs','']
    for app_label in settings.CUSTOM_INSTALLED_APPS:
        try:
            model = apps.get_model(app_label=app_label, model_name=name) 
            return model
        except LookupError:
            # no such model in this application
            pass
            
def get_conf(request, kwargs):
    # if 'model_name' in kwargs and kwargs['model_name'] in model_conf.keys():
        # conf = model_conf[kwargs['model_name']]
        model = get_model(kwargs['model_name'])
        if model: 
            model_name:str = model._meta.verbose_name or kwargs['model_name'].capitalize()
            form =  get_form(model)
            is_single = getattr(model,'is_single',False)
            return {"model":model, "form":form, "model_name": model_name,"single": is_single}
    
    # else:
    #     # messages.error(request, "Page not found!")
    #     return redirect("admin_dashboard")


class Dashboard(LoginRequiredMixin, View ):
    def get(self, request):
        tasks = Task.objects.all()
        task_data = {
            'all':tasks.count(),
            'done':tasks.filter(status = 'Completed').count(),
            'progress':tasks.filter(status ='Inprogress').count(),
            'pending':tasks.filter(status='Pending').count()
        }
        jobs = Job.objects.all()
        applications = Application.objects.count()
        events = Event.objects.all()
        return render(request, 'staff/admin_home.html', {'tasks':task_data, 'jobs':jobs, 'applications':applications, 'events':events})
    
    

class CreateView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        config = get_conf(self.request, self.kwargs)
        if not isinstance(config,dict):
            return redirect("admin_dashboard")
        
        # if config.isinstance()
        model, model_name  = config["model"], config["model_name"] 
        form = config["form"] 
        if config["single"] and model.objects.first(): # if model object has to be generated only once
            return redirect("change_view", model_name = kwargs['model_name'], pk=model.objects.first().id)
        
        return render(self.request, 'staff/create_page.html', { 'add':True,  'form':form, 'is_single':config["single"], 
                                                                'model_name':model_name.capitalize(),})
    
    def post(self, *args, **kwargs):
        config = get_conf(self.request, self.kwargs)
        model = config["model"]
        form = config["form"](self.request.POST, self.request.FILES)
        if form.is_valid():
            obj  = form.save(commit = False)
            if hasattr(model, 'created_by'):
                setattr(obj, 'created_by', self.request.user)
            obj.save()
            messages.success(self.request, f"Successfully created !")
            if config['single']:
                return redirect("admin_dashboard" )
            return redirect("list_view", model_name = self.kwargs['model_name'])

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
            messages.success(self.request, f"Successfully updated {model_name}!")
            if config['single']:
                return redirect("admin_dashboard" )
            return redirect("list_view", model_name = self.kwargs['model_name'])
        
        return render(self.request, 'staff/create_page.html', { 'add':False,  'form':form, 'is_single':config['single'], 
                                                                'model_name':model_name.capitalize(),})
    

class ListView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        # messages.success(self.request, "yo man")
        config = get_conf(self.request,self.kwargs)
        model, formal_name = config["model"], config["model_name"]
        # if model is single, just bring the first object
        if config['single']:
            return redirect("create_view", model_name = self.kwargs['model_name'])
        
        objs = model.objects.all()
        list_fields = getattr(model, 'list_fields',[])
        return render(self.request, "staff/list_page.html", 
                      {'model_name':formal_name, 'model_code':self.kwargs['model_name'], 'single':config['single'],
                       'objs':objs,'fields':list_fields}
                    ) 


class DeleteView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        config = get_conf(self.request,self.kwargs)
        model, model_name = config["model"], config["model_name"]
        
        # if model is single, just bring the first object
        if config['single']:
            print("Can't be deleted!")
            return redirect("admin_dashboard")
    
        obj = model.objects.get(id=self.kwargs['pk'])
        obj.delete()
        messages.success(self.request, f"Successfully deleted {model_name}")
        return redirect("list_view",model_name=self.kwargs['model_name'])
        
        
