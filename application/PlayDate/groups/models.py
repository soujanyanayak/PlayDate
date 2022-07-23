# •••••••••••••••••••••••••••
# ░█▄█░█▀█░█▀▄░█▀▀░█░░░█▀▀
# ░█░█░█░█░█░█░█▀▀░█░░░▀▀█
# ░▀░▀░▀▀▀░▀▀░░▀▀▀░▀▀▀░▀▀▀

# Contributor(s): AndrewC,
# Version: 1.2.0
# Homepage: http://bedev.playdate.surge.sh/docs/groups/models
# Description: These models reflect group tables and their related entities
# •••••••••••••••••••••••••••
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# from events.models import Event


class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=64, default=None, blank=True)
    group_admin = models.ForeignKey(
        User, default=None, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now=True)
    group_desc = models.TextField(
        max_length=256, null=True, blank=True, default=None)

    banner = models.ImageField(
        upload_to="group_banner", default=None, blank=True)

    # Django-Taggit: This ties to the Groups and Taggit Tables
    # tags are delimited by commas
    tags = TaggableManager()


class Member(models.Model):
    # Refactor this to Groupuser
    member_id = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    group_id = models.ForeignKey(
        Group, to_field='group_id', default=None, on_delete=models.CASCADE)
    join_date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('group_id', 'member_id',)
    #isAdmin = models.BooleanField(default=False)


class Groupadmin(models.Model):
    group_admin_id = models.IntegerField(primary_key=True)
    group_user = models.ForeignKey(Member, models.DO_NOTHING)

    class Meta:
        # managed = False
        db_table = 'GroupAdmin'
        unique_together = (('group_admin_id', 'group_user'),)


# The code for Event is already written in events>models.py
# class groupEvent(events.models.Event):

# •••••••••••••••••••••••••••••••••••••••••••••••••••
# ░█▀█░█▀▄░█▀▀░█░█░▀█▀░█░█░█▀▀░█▀▄░░░█▀▀░█▀█░█▀▄░█▀▀
# ░█▀█░█▀▄░█░░░█▀█░░█░░▀▄▀░█▀▀░█░█░░░█░░░█░█░█░█░█▀▀
# ░▀░▀░▀░▀░▀▀▀░▀░▀░▀▀▀░░▀░░▀▀▀░▀▀░░░░▀▀▀░▀▀▀░▀▀░░▀▀▀
# •••••••••••••••••••••••••••••••••••••••••••••••••••

# JoinGroup is a view function not a model class
# class Joingroup(models.Model):
#    join_group_id = models.IntegerField(primary_key=True)
#    user = models.ForeignKey(User, models.DO_NOTHING)
#    group = models.ForeignKey(Group, models.DO_NOTHING, blank=True, null=True)
#    datetime = models.DateTimeField()
#
#    class Meta:
#        # managed = False
#        db_table = 'JoinGroup'
#
#
# ManageGroupUser is a view function not a model class
# class Managegroupuser(models.Model):
#    manage_id = models.IntegerField(primary_key=True)
#    group_admin = models.ForeignKey(Groupadmin, models.DO_NOTHING, blank=True, null=True)
#    join_group = models.ForeignKey(Joingroup, models.DO_NOTHING, blank=True, null=True)
#    operation = models.CharField(max_length=45)
#
#    class Meta:
#        # managed = False
#        db_table = 'ManageGroupUser'
#
# class Group(models.Model):
#    group_id = models.IntegerField(primary_key=True)
#    group_admin = models.ForeignKey(Groupadmin, models.DO_NOTHING)
#    group_name = models.CharField(max_length=45)
#    group_desc = models.CharField(max_length=200)
#    create_date = models.DateTimeField()
#    group_size = models.IntegerField()
#
#    class Meta:
#        db_table = 'Group'


# class Groupuser(models.Model):
# Already implemented under 'Member'
# This is equivalent to Member
#    group_user_id = models.IntegerField(primary_key=True)
#    user = models.ForeignKey(User, models.DO_NOTHING)
#
#    class Meta:
#        # managed = False
#        db_table = 'GroupUser'
#        unique_together = (('group_user_id', 'user'),)
