from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import JobForm
from .models import Job
def add_vacancy(request):
    return render(request, 'job_post_add.html')
from django.shortcuts import render, redirect
from .forms import JobForm, ApplicationForm  # Assuming your form is in a file named forms.py
from .models import Job, Application
from django.shortcuts import get_object_or_404
from django.views import View
from core.models import Settings 
from django.core.mail import EmailMultiAlternatives, send_mail


#new from yismu

def job_list_ytemplate(request):
    search = request.GET.get('search', None)
    if search:
        jobs = Job.objects.filter(Status = 'Active', job_title__icontains = search, 
                                  job_description__icontains=search, skills__icontains = search )
    else:
        jobs = Job.objects.filter(Status = 'Active')
    return render(request, 'front/vacancy.html', {'jobs': jobs, 'search':search})
    
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


class jobs_apply(View):
    def get(self, *args, **kwargs):
        self.request.path
        job = Job.objects.get(id = self.kwargs['pk'])
        form = ApplicationForm()
        return render(self.request, 'front/vacancy_apply.html', {'form':form, 'job':job} )
    
    def post(self, *args, **kwargs):
        form = ApplicationForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            ap = form.save(commit=False)
            ap.job =Job.objects.get(id = self.kwargs['pk'])
            ap.save()

            msg = f"An applicant named {ap.name} has submitted an application for the job: {ap.job} "
            email = "antenyismu@gmail.com"
            # email = Settings.objects.first().email_for_contact_us if Settings.objects.first() else 'mukeraacc@gmail.com'
            e = EmailMultiAlternatives(f"New Job Application from : {ap.name}",msg,from_email="Kanenus",to=[str(email)], )
            # e.attach("Cv file",ap.cv)
            m = e.send()
            print(m)

            messages.success(self.request, ("Applied Successfully."))
            return redirect('/vacancies/job_list/')
        
        messages.error(self.request, "Invalid Data")
        return render(self.request, 'front/vacancy_apply.html', {'form':form} )
    

def update_vacancy(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_list_admin')
    else:
        form = JobForm(instance=job)

    context = {
        'form': form,
        'job': job,
    }
    return render(request, 'update_vacancy.html', context)