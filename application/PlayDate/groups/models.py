from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Group(models.Model):
    groupID = models.AutoField(primary_key=True)
    groupName = models.CharField(max_length=64, default=None, blank=True)
    groupAdminID = models.ForeignKey(
        User, default=None, on_delete=models.CASCADE)
    createDate = models.DateTimeField(auto_now=True)
    groupDesc = models.TextField(
        max_length=256, null=True, blank=True, default=None)


class Member(models.Model):
    memberID = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    groupID = models.ForeignKey(
        Group, to_field='groupID', default=None, on_delete=models.CASCADE)
    joinDate = models.DateTimeField(auto_now=True)
    #isAdmin = models.BooleanField(default=False)
