from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    task_description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False)
    key_tasks = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False)

    # Use DateTimeInput widget for assigned_date and due_date
    assigned_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    due_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Task
        fields = ['task_name', 'assigned_to','assigned_date', 'due_date', 'status', 'priority', 'task_description', 'key_tasks']

    def clean(self):
        cleaned_data = super().clean()
        assigned_date = cleaned_data.get('assigned_date')
        due_date = cleaned_data.get('due_date')

        # Ensure start date is less than end date
        if assigned_date and due_date and assigned_date >= due_date:
            raise forms.ValidationError("The start date must be less than the end date.")

        return cleaned_data
# forms.py
class CommentForm(forms.Form):
    comment_content = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write a comment...'}))
