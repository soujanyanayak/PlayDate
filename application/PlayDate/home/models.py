from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class generalUser(models.Model):
    trackingID = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=50)


class Account(models.Model):
    gender_choices = [
        ('FEMALE', 'Female'),
        ('MALE', 'Male'),
        ('NON_BINARY', 'Non-Binary'),
    ]
    accountID = models.AutoField(primary_key=True)
    gender = models.CharField(
        max_length=10, choices=gender_choices)
    # fname=models.CharField(max_length = 30)
    # lname=models.CharField(max_length = 30)
    dob = models.DateField(max_length=11)
    date_joined = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)
