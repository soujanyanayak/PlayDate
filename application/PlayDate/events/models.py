# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Publicevent(models.Model):
    public_event_id = models.IntegerField(primary_key=True)
    address = models.ForeignKey('Address', models.DO_NOTHING)
    event_url = models.CharField(max_length=1000)
    name = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'PublicEvent'



class Address(models.Model):
    address_id = models.IntegerField(primary_key=True)
    street = models.CharField(max_length=100)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=45)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Address'


class Location(models.Model):
    country_code = models.TextField(blank=True, null=True)
    zipcode = models.IntegerField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state_name = models.TextField(blank=True, null=True)
    state_code = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Location'
