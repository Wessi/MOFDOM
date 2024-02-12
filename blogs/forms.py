from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'category', 'publish_date', 'publish_time', 'content', 'images']
        # Add any additional fields from your Blog model that you want to include in the form

    # You can add additional form field validation or customization here if needed
