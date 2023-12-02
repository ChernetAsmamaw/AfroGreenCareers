from django.db import models
from users.models import User


class Resume(models.Model):
    background_type_options = (
        ('Diploma', 'Diploma'),
        ('Certificate', 'Certificate'),
        ('Undergraduate', 'Undergraduate'),
        ('Postgraduate', 'Postgraduate')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fist_name = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    job_title = models.CharField(max_length=100, null=True, blank=True)
    academic_background =  models.CharField(max_length=20, choices=background_type_options, null=True, blank=True)
    upload_resume = models.FileField(upload_to='resume/', null = True, blank = True)


    def __str__(self):
        return f'{self.first_name} {self.surname}'