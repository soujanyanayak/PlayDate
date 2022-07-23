#•••••••••••••••••••••••••••••••••#
# ░█▀▀░█▀█░█▀▄░█▄█░█▀▀
# ░█▀▀░█░█░█▀▄░█░█░▀▀█
# ░▀░░░▀▀▀░▀░▀░▀░▀░▀▀▀
# Contributor(s): AndrewC,
# Version: 1.0.0
# Homepage: http://bedev.playdate.surge.sh/docs/groups/forms
# Description:Each model that is editable by users needs to have a form that points to that particular model.
#•••••••••••••••••••••••••••••••••#
from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import DateInput
from . import models


class joinGroupForm(ModelForm):
    # This is an empty form and is used only to connect views<->models
    class Meta:
        model = models.Member
        fields = []


class createGroupForm(ModelForm):
    class Meta:
        model = models.Group
        fields = ['group_name', 'group_desc', 'tags', 'banner']
        labels = {
            'group_name': ('Group Name'), 'group_desc': ('Group Description'), 'tags': ("Enter keywords separated by a space; These words will help users to find your group.")
        }
        widgets = {
            'group_name': forms.TextInput(attrs={'style': 'width:65vw;', 'placeholder': "e.g. San Francisco Dog Group"}),
            'group_desc': forms.Textarea(attrs={'style': 'width:65vw;', 'placeholder': "Enter a brief description on what your group is all about!"}),
            'tags': forms.TextInput(attrs={'style': 'width:65vw;', 'placeholder': "dogs, dog, canine, canines, shiba inu, shiba-inu, shiba inu"}),
            # 'banner': forms.ImageField(),

        }


class memberListForm(ModelForm):
    # This is an empty form because users cannot edit the Member table
    class Meta:
        model = models.Member
        fields = []
