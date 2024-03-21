from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import JobForm
from .models import Job
def add_vacancy(request):
    return render(request, 'job_post_add.html')
from django.shortcuts import render, redirect
from .forms import JobForm  # Assuming your form is in a file named forms.py
from .models import Job
from django.shortcuts import get_object_or_404


#new from yismu

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'front/vacancy.html', {'jobs': jobs})
    
def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    
    if request.method == 'POST':
        job.delete()
        return redirect('job_list_admin')  # Assuming 'job_list' is the URL name for the job list view
    
    context = {'job': job}
    return render(request, 'delete_vacancy.html', context)

def post_job_view(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list_admin')  # Redirect to a success page after form submission
    else:
        form = JobForm()

    return render(request, 'job_post_add.html', {'form': form})

def job_list(request):
    jobs = Job.objects.all()
    context = {
        'jobs': jobs,
    }
    return render(request, 'job_list.html', context)

def jobs_view(request):
    return render(request, 'job_view_all.html')
def vacancy_board(request):
    # Fetch all jobs from the database
    jobs = Job.objects.all()
    # Pass the jobs to the template
    context = {'jobs': jobs}
    return render(request, 'vacanacy_board.html', context)
def jobs_detail(request, job_id):
    try:
        job = Job.objects.get(id=job_id)
        key_responsibilities = job.job_description.split('\n')
        return render(request, 'vacancies_detail.html', {'job': job, 'key_responsibilities': key_responsibilities})
    except Job.DoesNotExist:
        # Job not found, render an empty page or display a message
        return render(request, 'job_list.html')  
def job_list_admin(request):
    vacancies = Job.objects.all()
    return render(request, 'job_list_admin.html', {'vacancies': vacancies})

