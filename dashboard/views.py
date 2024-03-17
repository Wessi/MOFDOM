from django.views import View
from django.shortcuts import render,redirect
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import *


class Dashboard(LoginRequiredMixin, View ):
    def get(self, request):
        return render(request, 'admin_home.html')
    
    