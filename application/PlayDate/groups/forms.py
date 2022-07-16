from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import DateInput
from . import models


class joinGroupForm(ModelForm):
    class Meta:
        model = models.Member
        fields = []


class createGroupForm(ModelForm):
    class Meta:
        model = models.Group
        fields = ['group_name', 'group_desc', 'tags']
        labels = {
            'group_name': ('Group Name'), 'group_desc': ('Group Description'), 'tags': ("Enter keywords separated by a space; These words will help users to find your group.")
        }


class memberListForm(ModelForm):
    class Meta:
        model = models.Member
        fields = []
