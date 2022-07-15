from django.db import models
from django.contrib.auth.models import User
# from events.models import Event
# Create your models here.


# class Group(models.Model):
#     groupID = models.AutoField(primary_key=True)
#     groupName = models.CharField(max_length=64, default=None, blank=True)
#     groupAdminID = models.ForeignKey(
#         User, default=None, on_delete=models.CASCADE)
#     createDate = models.DateTimeField(auto_now=True)
#     groupDesc = models.TextField(
#         max_length=256, null=True, blank=True, default=None)

#Group users
# class Member(models.Model):
#     memberID = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
#     groupID = models.ForeignKey(
#         Group, to_field='groupID', default=None, on_delete=models.CASCADE)
#     joinDate = models.DateTimeField(auto_now=True)
#     #isAdmin = models.BooleanField(default=False)


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


class Group(models.Model):
    group_id = models.IntegerField(primary_key=True)
    group_admin = models.ForeignKey(Groupadmin, models.DO_NOTHING)
    group_name = models.CharField(max_length=45)
    group_desc = models.CharField(max_length=200)
    create_date = models.DateTimeField()
    group_size = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'Group'


class Joingroup(models.Model):
    join_group_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    group = models.ForeignKey(Group, models.DO_NOTHING, blank=True, null=True)
    datetime = models.DateTimeField()

    class Meta:
        # managed = False
        db_table = 'JoinGroup'


class Managegroupuser(models.Model):
    manage_id = models.IntegerField(primary_key=True)
    group_admin = models.ForeignKey(Groupadmin, models.DO_NOTHING, blank=True, null=True)
    join_group = models.ForeignKey(Joingroup, models.DO_NOTHING, blank=True, null=True)
    operation = models.CharField(max_length=45)

    class Meta:
        # managed = False
        db_table = 'ManageGroupUser'

