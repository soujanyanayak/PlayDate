from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# from events.models import Event
# Create your models here.


class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=64, default=None, blank=True)
    group_admin = models.ForeignKey(
        User, default=None, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now=True)
    # Group_tags, as of now it is going to be space-delminited column of tags used for searching.
    #group_tags = models.TextField(max_length=512, default=None, blank=True)
    group_desc = models.TextField(
        max_length=256, null=True, blank=True, default=None)

    # Django-Taggit
    tags = TaggableManager()


class Member(models.Model):
    member_id = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    group_id = models.ForeignKey(
        Group, to_field='group_id', default=None, on_delete=models.CASCADE)
    join_date = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('group_id', 'member_id',)
    #isAdmin = models.BooleanField(default=False)


# class Group(models.Model):
#    group_id = models.IntegerField(primary_key=True)
#    group_admin = models.ForeignKey(Groupadmin, models.DO_NOTHING)
#    group_name = models.CharField(max_length=45)
#    group_desc = models.CharField(max_length=200)
#    create_date = models.DateTimeField()
#    group_size = models.IntegerField()
#
    class Meta:
#        # managed = False
       db_table = 'Group'


class Groupuser(models.Model):
    group_user_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)

    class Meta:
        # managed = False
        db_table = 'GroupUser'
        unique_together = (('group_user_id', 'user'),)


class Groupadmin(models.Model):
    group_admin_id = models.IntegerField(primary_key=True)
    group_user = models.ForeignKey(Groupuser, models.DO_NOTHING)

    class Meta:
        # managed = False
        db_table = 'GroupAdmin'
        unique_together = (('group_admin_id', 'group_user'),)


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
