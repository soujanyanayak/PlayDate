# ░█▀▀░█▀█░█▀▄░█▄█░█▀▀
# ░█▀▀░█░█░█▀▄░█░█░▀▀█
# ░▀░░░▀▀▀░▀░▀░▀░▀░▀▀▀

# Each model that is editable by users needs to have a form that points to that
# particular model.

from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import DateInput
from . import models

# This is an empty form and is used only to connect views<->models


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

# This is an empty form because users cannot edit the Member table


class memberListForm(ModelForm):
    class Meta:
        model = models.Member
        fields = []
