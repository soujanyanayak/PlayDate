# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Location(models.Model):
    country_code = models.CharField(max_length=2, blank=True, null=True)
    zipcode = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=180, blank=True, null=True)
    state_name = models.CharField(max_length=45, blank=True, null=True)
    state_code = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location'


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=10, blank=True, null=True)
    event_start = models.DateTimeField(blank=True, null=True)
    event_end = models.DateTimeField(blank=True, null=True)
    street_address = models.CharField(max_length=500, blank=True, null=True)
    location = models.ForeignKey(Location, models.DO_NOTHING, db_column='location', blank=True, null=True)
    type = models.CharField(max_length=2, blank=True, null=True)
    url = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event'

class citysuggestion(models.Model):
    name = models.CharField(max_length=100)
  
    def __str__(self):
        return f"{self.name}"