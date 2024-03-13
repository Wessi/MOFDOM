from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'blog_category', 'publish_date', 'publish_time', 'content', 'images']
        # Add any additional fields from your Blog model that you want to include in the form

    