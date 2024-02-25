from django import forms
from django.contrib.auth.models import User
from .models import Footer
from django import forms
from .models import GalleryImage
from . import models
from .models import *

#for admin signup
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'password']
        widgets = {
        'password': forms.PasswordInput()
        }


class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
class FooterForm(forms.ModelForm):
    class Meta:
        model = Footer
        fields = '__all__'
class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['title', 'category', 'image']

    # Adding a custom widget for the 'category' field
    category = forms.ChoiceField(choices=GalleryImage.CATEGORY_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))



class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'image', 'time', 'location', 'description', 'date']

class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question', 'answer']

        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your question'}),
            'answer': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your answer'}),
        }