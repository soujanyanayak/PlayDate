from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import DateInput
from . import models


class createGroupForm(ModelForm):
    class Meta:
        model = models.Group
        fields = ['group_name', 'group_desc']
        labels = {
            'groupName': ('Group Name'), 'groupDesc': ('Group Description')
        }


class memberListForm(ModelForm):
    class Meta:
        model = models.Groupuser
        fields = []
