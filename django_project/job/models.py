from django.db import models
from users.models import User
from company.models import Company


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Industry(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Job(models.Model):
    job_env_options = (
        ('Remote', 'Remote'),
        ('In-Person', 'In-Person'),
        ('Hybrid', 'Hybrid')
    )

    job_type_options = (
        ('Full-Time Job', 'Full-Time Job'),
        ('Part-Time Job', 'Part-Time Job'),
        ('Full-Time Internship', 'Full-Time Internship'),
        ('Part-Time Internship', 'Part-Time Internship')   
    )

    duration = (
        ('3-Months', '3-Months'),
        ('4-Months', '4-Months'),
        ('6-Months', '6-Months'),
        ('Contract', 'Contract'),  
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    salary = models.PositiveIntegerField(default=5000)
    requirements = models.TextField(null=True, blank=True)
    ideal_candidate = models.TextField(null=True, blank=True)
    deadline = models.DateField(null=True)
    field = models.CharField(max_length=100, null=True, blank=True)
    is_avaliable = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    industry = models.ForeignKey(Industry, on_delete=models.DO_NOTHING, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    job_env = models.CharField(max_length=20, choices=job_env_options, null=True, blank=True)
    job_type = models.CharField(max_length=20, choices=job_type_options, null=True, blank=True)
    duration = models.CharField(max_length=20, choices=duration, null=True, blank=True)


    def __str__(self):
        return self.title


class ApplyJob(models.Model):
    status_choices = (
        ('Accepted', 'Accepted'),
        ('Declined', 'Declined'),
        ('Pending', 'Pending')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=status_choices)
    