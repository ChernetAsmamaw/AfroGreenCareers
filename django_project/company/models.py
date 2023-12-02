from django.db import models
from users.models import User


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    est_date = models.PositiveIntegerField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    call_adress = models.CharField(max_length=20, null=True, blank=True)
    company_industry = models.CharField(max_length=100, null=True, blank=True)
    company_mission = models.TextField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.name
