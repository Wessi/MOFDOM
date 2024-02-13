from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = []  # Exclude any fields you don't want to include in the form
        widgets = {
            'job_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job Title'}),
            'job_type': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'vacancies': forms.Select(attrs={'class': 'form-control'}),
            'skills': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Skills'}),
            'job_deadline': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'locationn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'level': forms.Select(attrs={'class': 'form-control'}),
        }
