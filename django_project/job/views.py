from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Job, ApplyJob
from .form import CreateJobForm, UpdateJobForm

# Create a job/internship opening 
def create_job(request):
    if request.user.is_recruiter and request.user.has_company:
        if request.method == 'POST':
            form = CreateJobForm(request.POST)
            if form.is_valid():
                var = form.save(commit=False)
                var.user = request.user
                var.company = request.user.company
                var.save()
                messages.info(request, 'New opening has been created!')
                return redirect('dashboard')
            else:
                messages.warning(request, 'Something went wrong!')
                return redirect('create-job')
        else:
            form = CreateJobForm()
            context = {'form':form}
            return render(request, 'job/create_job.html', context)
    else:
        messages.warning(request, 'Permission denied!')
        return redirect('dashboard')


# Update details of a job/internship opening 
def update_job(request, pk):
    if request.user.is_recruiter and request.user.has_company:
        job = Job.objects.get(pk=pk)
        if request.method == 'POST':
            form = UpdateJobForm(request.POST, instance=job)
            if form.is_valid():
                form.save()
                messages.info(request, 'Your opening info has been succesfully updated!')
                return redirect('dashboard')
            else:
                messages.warning(request, 'Something went wrong!')
        else:
            form = UpdateJobForm(instance=job)
            context = {'form':form}
            return render(request, 'job/update_job.html', context)
    else:
        messages.warning(request, 'Permission denied!')
        return redirect('dashboard')

# Manage job applications
def manage_jobs(request):
    jobs = Job.objects.filter(user=request.user, company=request.user.company)
    context = {'jobs':jobs}
    return render(request, 'job/manage_jobs.html', context)

# Apply to jobs
def apply_to_job(request, pk):
    if request.user.is_authenticated:
        job = Job.objects.get(pk=pk)
        if ApplyJob.objects.filter(user=request.user, job=pk).exists():
            messages.warning(request, 'Permission denied!')
            return redirect('dashboard')
        else :
            ApplyJob.objects.create(
                job=job,
                user = request.user,
                status = 'Pending'
            )
            messages.info(request, 'You have succesfuly completed your application! please see your dashboard.')
            return redirect('dashboard')
    else:
        messages.info(request, 'Please login to continue!')
        return redirect ("login")
    

def all_applicants(request, pk):
    job = Job.objects.get(pk=pk)
    if request.user.is_authenticated and request.user.is_recruiter and job.company.user == request.user:
        applied_jobs = ApplyJob.objects.filter(job = job)
        context = {'job':job, 'applied_jobs':applied_jobs}
        return render(request, 'job/all_applicants.html', context)
    else:
        messages.warning(request, 'Permission Denied')
        return redirect('dashboard')
    


def applied_jobs(request):
    jobs = ApplyJob.objects.filter(user=request.user)
    context = {'jobs':jobs}
    return render(request, 'job/applied_job.html', context)