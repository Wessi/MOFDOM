from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from .forms import TaskForm
from django.views import View
from django.utils import timezone
from .forms import CommentForm, TaskForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
def task_list_view(request, type):
    user = request.user
    if type == 'Assigned':
        tasks = user.assigned_tasks.all()
    elif type == 'Monitoring':
        tasks = user.monitoring_tasks.all()
    elif type == 'All':
        tasks = Task.objects.all()
    context = {
        'tasks': tasks, 'form':TaskForm(), 'type':type
    }
    return render(request, 'task-list-view.html', context)
    # return render(request, 'some.html', context)

def create_task(request):
    if request.method == 'POST':
        print("--------")
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            
            print("not working",form.errors)
        
        return redirect('task_list_view')

    else:
        print("+++++")
        form = TaskForm()
    return redirect('task_list_view')


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task.delete()
        return redirect('task_list_view')  # Redirect to your task list view after deletion

    context = {
        'task': task,
    }
    return render(request, 'delete_task.html', context)
def task_details(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    context = {
        'task': task,
    }
    return render(request, 'task_details_admin.html', context)
class TaskDetailsView(View):
    template_name = 'task_details_admin.html'

    def get_context_data(self, task_id):
        task = get_object_or_404(Task, id=task_id)

        # Assuming you have the currently logged-in user
        assigned_by_user = self.request.user

        # Calculate progress based on due date and current date
        total_days = (task.due_date - task.assigned_date).days
        remaining_days = (task.due_date - timezone.now()).days
        progress = int((total_days - remaining_days) / total_days * 100)

        context = {
            'task': task,
            'assigned_by_user': assigned_by_user,
            'progress': progress,
        }

        return context

    def get(self, request, task_id):
        context = self.get_context_data(task_id)
        return render(request, self.template_name, context)

def get_key_tasks(task):
    return task.key_tasks.split('\n') if task.key_tasks else []
@login_required
def add_comment(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            user_profile = request.user
            content = form.cleaned_data['comment_content']
            comment = Comment.objects.create(task=task, user=user_profile, content=content)
            return HttpResponseRedirect(request.path_info)  # Redirect to the same page after posting comment
    else:
        form = CommentForm()
    context = {
        'task': task,
        'form': form,
    }
    return render(request, 'task_details_admin.html', context)

@login_required
def reply_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    task_id = comment.task.id  # Get the task id associated with the comment
    task = comment.task  # Retrieve the task object
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            user_profile = request.user  # Retrieve the UserProfile object associated with the authenticated user
            content = form.cleaned_data['comment_content']
            # Assuming you have a field to store the parent comment in your Comment model
            reply = Comment.objects.create(task=comment.task, user=user_profile, content=content, parent_comment=comment)
            return redirect('add_comment', task_id=task_id)  # Redirect to task detail page
    else:
        form = CommentForm()
    context = {
        'form': form,
        'task': task,  # Pass the task object to the template context
    }
    return render(request, 'task_details_admin.html', context)


def notifications_view(request):
    # Retrieve notifications for the current user and order them by creation date
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')

    # Pass notifications to the template
    context = {
        'notifications': notifications,
    }

    return render(request, 'base_new_admin.html', context)