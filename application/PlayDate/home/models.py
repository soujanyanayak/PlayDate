# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.


class Address(models.Model):
    address_id = models.IntegerField(primary_key=True)
    street = models.CharField(max_length=45)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=45)
    zipcode = models.IntegerField()


class generalUser(models.Model):
    trackingID = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=50)

    class Meta:
        db_table = 'generalUser'


class Account(models.Model):
    gender_choices = [
        ('FEMALE', 'Female'),
        ('MALE', 'Male'),
        ('NON_BINARY', 'Non-Binary'),
    ]
    #accountID = models.AutoField(primary_key=True)
    accountID = models.ForeignKey(
        User, default=None, unique=True, on_delete=models.CASCADE, primary_key=True)
    gender = models.CharField(
        max_length=10, choices=gender_choices)
    # fname=models.CharField(max_length = 30)
    # lname=models.CharField(max_length = 30)
    dob = models.DateField(max_length=11)
    date_joined = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Account'


class Profile(models.Model):
    profileID = models.ForeignKey(
        User, default=None, on_delete=models.CASCADE, primary_key=True)
    profileDesc = models.TextField(
        max_length=256, null=True, blank=True, default=None)
    avatar = models.ImageField(
        upload_to="uploads", default=None, blank=True)

    class Meta:
        db_table = 'Profile'
